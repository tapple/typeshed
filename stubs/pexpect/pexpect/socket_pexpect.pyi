import socket
from typing import Iterable

from .spawnbase import SpawnBase, _Logfile

class SocketSpawn(SpawnBase):
    def __init__(
        self,
        socket: socket.socket,
        args: None = None,
        timeout: int = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ): ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def send(self, s: str | bytes) -> int: ...
    def sendline(self, s: str | bytes) -> int: ...
    def write(self, s: str | bytes) -> None: ...
    def writelines(self, sequence: Iterable[str | bytes]) -> None: ...
    def read_nonblocking(self, size: int = 1, timeout: int | None = -1) -> bytes: ...
