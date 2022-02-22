from os import path
from subprocess import check_output
from tempfile import mkdtemp


def solc(base: str, relpath: str):

    input = path.join(base, relpath)
    assert path.isfile(input)
    output = mkdtemp()
    cmd = [
        'docker',
        'run',
        '-v', ':'.join([base, '/input', 'ro']),
        '-v', ':'.join([output, '/output', 'z']),
        'docker.io/ethereum/solc:stable',
        '-o', '/output',
        '--abi',
        '--bin',
        path.join('/input', relpath),
    ]
    check_output(cmd)
    return output
