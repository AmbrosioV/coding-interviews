from os import listdir, path
from os.path import isfile, join
import sys
from BankStatement import BankStatement


def listDir(path):
    """
    List files in 'path' directory
    Params
    -------
    path : str
        relative path to search for files
    Returns : list of str
    -------
        returns a list of string with file names
    """
    return [f for f in listdir(path) if isfile(join(path, f))]


if __name__ == '__main__':
    dir_path = path.dirname(path.realpath(__file__))
    try:
        path = join(dir_path, 'cartolas', sys.argv[1])
    except IndexError:
        print('Evaluating for empresa_A as no input was received')
        path = join(dir_path, 'cartolas', 'empresa_A')

    empresa_A = BankStatement(path)

    for filepath in listDir(path):
        empresa_A.update(filepath)

    empresa_A.show_movements()
