# common code block with psutil

import os
import psutil
import signal

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls

def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True, timeout=None, on_terminate=None):
    """
    Kill a process tree (including grandchildren) with signal "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callback function whihc is called as soon as a child terminates.
    """
    if pid == os.getpid():
        raise RuntimeError("I am tried to kill myself.")
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent == True:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout, callback=on_terminate)

    return (gone, alive)

def reap_children(timeout=3):
    """
    Tries hard to terminate and ultimately kill all the children of this process.
    """
    def on_terminate(proc):
        print("process {} terminated with exit code {}".format(proc, proc.returncode))
    
    procs = psutil.Process().children()
    # Send death
    for p in procs:
        p.terminate()
    gone, alive = psutil.wait_procs(procs, timeout=timeout)

    if alive:
        # Send Death
        for p in alive:
            print("process {} survived SIGTERM; trying SIGKILL" % p)
            p.kill()
        gone, alive = psutil.wait_procs(alive, timeout=timeout, callback=on_terminate) 

        if alive:
            # give up
            for p in alive:
                print("process {} survived SIGKILL; giving up." % p) 
