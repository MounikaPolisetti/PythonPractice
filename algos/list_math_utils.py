# a is a list of numbers (floats)
# Returns min of the list
def min_of_list(a):
    # TODO(mounika): Write code here.
    if len(a) == 0:
        return None
    min = a[0]
    for x in a:
        if x < min:
            min = x

    return min


if __name__ == "__main__":
    print ("hello")


