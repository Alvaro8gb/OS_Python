The sequential average runs significantly faster than the threaded one across multiple runs.
My guess for why this happens is either the virtual machine I am running is poorly using
the 4 threads it has access to, or there isn't enough data to justify the performance
impact of creating the 4 threads.


Sequential Average 1:
Sequential Execution Time: 0.0007221698760986328 seconds

Threaded Average 1:
Threaded Execution Time (4 threads): 0.016740083694458008 seconds

Sequential Average 2:
Sequential Execution Time: 0.0008111000061035156 seconds

Threaded Average 2:
Threaded Execution Time (4 threads): 0.01336216926574707 seconds