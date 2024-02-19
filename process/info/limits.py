import resource

# Define resource constants
RLIMIT_CPU = resource.RLIMIT_CPU
RLIMIT_FSIZE = resource.RLIMIT_FSIZE
RLIMIT_DATA = resource.RLIMIT_DATA
RLIMIT_STACK = resource.RLIMIT_STACK
RLIMIT_CORE = resource.RLIMIT_CORE
RLIMIT_NPROC = resource.RLIMIT_NPROC
RLIMIT_NOFILE = resource.RLIMIT_NOFILE

# Function to get resource limit
def get_resource_limit(resource):
    soft_limit, hard_limit = resource.getrlimit(resource)
    print(f"Soft Limit for {resource}: {soft_limit}")
    print(f"Hard Limit for {resource}: {hard_limit}")

# Function to set resource limit
def set_resource_limit(resource, soft_limit, hard_limit):
    resource.setrlimit(resource, (soft_limit, hard_limit))
    print(f"Resource limits for {resource} set to: ({soft_limit}, {hard_limit})")

# Example usage
get_resource_limit(RLIMIT_CPU)

# Set a new resource limit (RLIM_INFINITY indicates unlimited)
set_resource_limit(RLIMIT_FSIZE, soft_limit=1024, hard_limit=2048)

# Verify the new limit
get_resource_limit(RLIMIT_FSIZE)