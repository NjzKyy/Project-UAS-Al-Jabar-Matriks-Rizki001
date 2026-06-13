def determinan3x3(m):
    """
    Menghitung determinan matriks 3x3
    Parameter:
        m = matriks 3x3 dalam bentuk list
    Return:
        determinan
    """

    det = (
        m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))
        - m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))
        + m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0]))
    )

    return det