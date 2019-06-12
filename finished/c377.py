'''
Challenge 377
https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
'''

def fit_boxes_no_rotate(X, Y, x, y):
    return int(X/x) * int(Y/y)

def fit_boxes_rotate_all(X, Y, x, y):
    return max(
        fit_boxes_no_rotate(X, Y, x, y),
        fit_boxes_no_rotate(X, Y, y, x),
    )

def fit_boxes_3D(X, Y, Z, x, y, z):

    def fit(X, Y, Z, x, y, z):
        return int(X/x) * int(Y/y) * int(Z/z)

    return max(
        fit(X, Y, Z, x, y, z),
        fit(X, Y, Z, y, z, x),
        fit(X, Y, Z, z, x, y),
        fit(X, Y, Z, x, z, y),
        fit(X, Y, Z, y, x, z),
        fit(X, Y, Z, z, y, x),
    )
