from _typeshed import Incomplete, SupportsRead, SupportsWrite, Unused
from collections.abc import Callable, Iterable, Iterator, MutableMapping, Sequence
from enum import IntEnum
from pathlib import Path
from typing import Any, ClassVar, Protocol, SupportsBytes
from typing_extensions import Literal, Self, TypeAlias

from PIL.PyAccess import PyAccess

from ._imaging import (
    DEFAULT_STRATEGY as DEFAULT_STRATEGY,
    FILTERED as FILTERED,
    FIXED as FIXED,
    HUFFMAN_ONLY as HUFFMAN_ONLY,
    RLE as RLE,
    _PixelAccessor,
)
from .ImageFilter import Filter
from .ImagePalette import ImagePalette

_Mode: TypeAlias = str
_Resample: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Size: TypeAlias = tuple[int, int]
_Box: TypeAlias = tuple[int, int, int, int]

_ConversionMatrix: TypeAlias = (
    tuple[float, float, float, float] | tuple[float, float, float, float, float, float, float, float, float, float, float, float]
)
# `str` values are only accepted if mode="RGB" for an `Image` object
# `float` values are only accepted for certain modes such as "F"
# See https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
_Color: TypeAlias = int | tuple[int] | tuple[int, int, int] | tuple[int, int, int, int] | str | float | tuple[float]

class _Writeable(SupportsWrite[bytes], Protocol):
    def seek(self, __offset: int) -> Any: ...

NORMAL: Literal[0]  # deprecated
SEQUENCE: Literal[1]  # deprecated
CONTAINER: Literal[2]  # deprecated

class DecompressionBombWarning(RuntimeWarning): ...
class DecompressionBombError(Exception): ...

MAX_IMAGE_PIXELS: int | None
USE_CFFI_ACCESS: Incomplete

LINEAR: Literal[Resampling.BILINEAR]  # deprecated
CUBIC: Literal[Resampling.BICUBIC]  # deprecated
ANTIALIAS: Literal[Resampling.LANCZOS]  # deprecated

def isImageType(t): ...

class Transpose(IntEnum):
    FLIP_LEFT_RIGHT: Literal[0]
    FLIP_TOP_BOTTOM: Literal[1]
    ROTATE_90: Literal[2]
    ROTATE_180: Literal[3]
    ROTATE_270: Literal[4]
    TRANSPOSE: Literal[5]
    TRANSVERSE: Literal[6]

# All Transpose items
FLIP_LEFT_RIGHT: Literal[0]
FLIP_TOP_BOTTOM: Literal[1]
ROTATE_90: Literal[2]
ROTATE_180: Literal[3]
ROTATE_270: Literal[4]
TRANSPOSE: Literal[5]
TRANSVERSE: Literal[6]

class Transform(IntEnum):
    AFFINE: Literal[0]
    EXTENT: Literal[1]
    PERSPECTIVE: Literal[2]
    QUAD: Literal[3]
    MESH: Literal[4]

# All Transform items
AFFINE: Literal[0]
EXTENT: Literal[1]
PERSPECTIVE: Literal[2]
QUAD: Literal[3]
MESH: Literal[4]

class Resampling(IntEnum):
    NEAREST: Literal[0]
    LANCZOS: Literal[1]
    BILINEAR: Literal[2]
    BICUBIC: Literal[3]
    BOX: Literal[4]
    HAMMING: Literal[5]

# All Resampling items
NEAREST: Literal[0]
LANCZOS: Literal[1]
BILINEAR: Literal[2]
BICUBIC: Literal[3]
BOX: Literal[4]
HAMMING: Literal[5]

class Dither(IntEnum):
    NONE: Literal[0]
    ORDERED: Literal[1]
    RASTERIZE: Literal[2]
    FLOYDSTEINBERG: Literal[3]

# All Dither items
NONE: Literal[0]
ORDERED: Literal[1]
RASTERIZE: Literal[2]
FLOYDSTEINBERG: Literal[3]

class Palette(IntEnum):
    WEB: Literal[0]
    ADAPTIVE: Literal[1]

# All Palette items
WEB: Literal[0]
ADAPTIVE: Literal[1]

class Quantize(IntEnum):
    MEDIANCUT: Literal[0]
    MAXCOVERAGE: Literal[1]
    FASTOCTREE: Literal[2]
    LIBIMAGEQUANT: Literal[3]

# All Quantize items
MEDIANCUT: Literal[0]
MAXCOVERAGE: Literal[1]
FASTOCTREE: Literal[2]
LIBIMAGEQUANT: Literal[3]

ID: list[str]
OPEN: dict[str, Any]
MIME: dict[str, str]
SAVE: dict[str, Any]
SAVE_ALL: dict[str, Any]
EXTENSION: dict[str, str]
DECODERS: dict[str, Any]
ENCODERS: dict[str, Any]

MODES: list[_Mode]

def getmodebase(mode: _Mode) -> Literal["L", "RGB"]: ...
def getmodetype(mode: _Mode) -> Literal["L", "I", "F"]: ...
def getmodebandnames(mode: _Mode) -> tuple[str, ...]: ...
def getmodebands(mode: _Mode) -> int: ...
def preinit() -> None: ...
def init() -> None: ...
def coerce_e(value) -> _E: ...

class _E:
    scale: Incomplete
    data: Incomplete
    def __init__(self, scale, data) -> None: ...
    def __neg__(self): ...
    def __add__(self, other) -> _E: ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other) -> _E: ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...

_ImageState: TypeAlias = tuple[dict[str, Any], str, tuple[int, int], Any, bytes]

class Image:
    format: ClassVar[str | None]
    format_description: ClassVar[str | None]
    im: Any
    mode: _Mode
    palette: Any
    info: dict[Any, Any]
    readonly: int
    pyaccess: PyAccess | None
    is_animated: bool  # not present on all Image objects
    n_frames: int  # not present on all Image objects
    # Only defined after a call to save().
    encoderconfig: tuple[Incomplete, ...]
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def size(self) -> tuple[int, int]: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def close(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def __array_interface__(self): ...
    def __getstate__(self) -> _ImageState: ...
    def __setstate__(self, state: _ImageState) -> None: ...
    def tobytes(self, encoder_name: str = "raw", *args) -> bytes: ...
    def tobitmap(self, name: str = "image") -> bytes: ...
    def frombytes(self, data: bytes, decoder_name: str = "raw", *args) -> None: ...
    def load(self) -> _PixelAccessor: ...
    def verify(self) -> None: ...
    def convert(
        self,
        mode: _Mode | None = None,
        matrix: _ConversionMatrix | None = None,
        dither: int | None = None,
        palette: Palette | Literal[0, 1] = ...,
        colors: int = 256,
    ) -> Image: ...
    def quantize(
        self,
        colors: int = 256,
        method: Quantize | Literal[0, 1, 2, 3] | None = None,
        kmeans: int = 0,
        palette: Image | None = None,
        dither: int = ...,
    ) -> Image: ...
    def copy(self) -> Image: ...
    __copy__ = copy
    def crop(self, box: _Box | None = None) -> Image: ...
    def draft(self, mode: _Mode, size: _Size) -> None: ...
    def filter(self, filter: Filter | Callable[[], Filter]) -> Image: ...
    def getbands(self) -> tuple[str, ...]: ...
    def getbbox(self) -> tuple[int, int, int, int] | None: ...
    def getcolors(self, maxcolors: int = 256) -> list[tuple[int, int]]: ...
    def getdata(self, band: int | None = None): ...
    def getextrema(self): ...
    def getexif(self) -> Exif: ...
    def get_child_images(self) -> list[Image]: ...
    def getim(self): ...
    def getpalette(self, rawmode: str | None = "RGB") -> list[int] | None: ...
    def apply_transparency(self) -> None: ...
    def getpixel(self, xy: tuple[int, int]): ...
    def getprojection(self) -> tuple[list[int], list[int]]: ...
    def histogram(self, mask: Image | None = None, extrema: tuple[int, int] | tuple[float, float] | None = None) -> list[int]: ...
    def entropy(self, mask: Image | None = None, extrema: tuple[int, int] | tuple[float, float] | None = None) -> float: ...
    def paste(self, im: Image | _Color, box: tuple[int, int] | _Box | None = None, mask: Image | None = None) -> None: ...
    def alpha_composite(self, im: Image, dest: tuple[int, int] = (0, 0), source: tuple[int, int] = (0, 0)) -> None: ...
    def point(self, lut, mode: _Mode | None = None) -> Image: ...
    def putalpha(self, alpha: Image | int) -> None: ...
    def putdata(self, data: Sequence[int], scale: float = 1.0, offset: float = 0.0) -> None: ...
    def putpalette(self, data: ImagePalette | bytes | Iterable[int] | SupportsBytes, rawmode: _Mode | None = "RGB") -> None: ...
    def putpixel(self, xy: tuple[int, int], value: _Color | list[float]) -> None: ...
    def remap_palette(self, dest_map: Iterable[int], source_palette: Sequence[int] | None = None) -> Image: ...
    def resize(
        self,
        size: tuple[int, int],
        resample: Resampling | _Resample | None = None,
        box: tuple[float, float, float, float] | None = None,
        reducing_gap: float | None = None,
    ) -> Image: ...
    def reduce(self, factor: int | tuple[int, int] | list[int], box: _Box | None = None) -> Image: ...
    def rotate(
        self,
        angle: float,
        resample: Resampling | _Resample = ...,
        expand: bool = ...,
        center: tuple[float, float] | None = None,
        translate: tuple[float, float] | None = None,
        fillcolor: _Color | None = None,
    ) -> Image: ...
    def save(
        self,
        fp: str | bytes | Path | _Writeable,
        format: str | None = None,
        *,
        save_all: bool = ...,
        bitmap_format: Literal["bmp", "png"] = ...,  # for ICO files
        optimize: bool = ...,
        **params: Any,
    ) -> None: ...
    def seek(self, frame: int) -> None: ...
    def show(self, title: str | None = None) -> None: ...
    def split(self) -> tuple[Image, ...]: ...
    def getchannel(self, channel: int | str) -> Image: ...
    def tell(self) -> int: ...
    def thumbnail(self, size: tuple[int, int], resample: Resampling | _Resample = ..., reducing_gap: float = 2.0) -> None: ...
    def transform(
        self,
        size: _Size,
        method: Transform | Literal[0, 1, 2, 3, 4],
        data=None,
        resample: Resampling | _Resample = ...,
        fill: int = 1,
        fillcolor: _Color | int | None = None,
    ) -> Image: ...
    def transpose(self, method: Transpose | Literal[0, 1, 2, 3, 4, 5, 6]) -> Image: ...
    def effect_spread(self, distance: int) -> Image: ...
    def toqimage(self): ...
    def toqpixmap(self): ...

class ImagePointHandler: ...
class ImageTransformHandler: ...

def new(mode: _Mode, size: tuple[int, int], color: _Color = 0) -> Image: ...
def frombytes(mode: _Mode, size: tuple[int, int], data, decoder_name: str = "raw", *args) -> Image: ...
def frombuffer(mode: _Mode, size: tuple[int, int], data, decoder_name: str = "raw", *args) -> Image: ...
def fromarray(obj, mode: _Mode | None = None) -> Image: ...
def fromqimage(im) -> Image: ...
def fromqpixmap(im) -> Image: ...
def open(
    fp: str | bytes | Path | SupportsRead[bytes], mode: Literal["r"] = "r", formats: list[str] | tuple[str, ...] | None = None
) -> Image: ...
def alpha_composite(im1: Image, im2: Image) -> Image: ...
def blend(im1: Image, im2: Image, alpha: float) -> Image: ...
def composite(image1: Image, image2: Image, mask: Image) -> Image: ...
def eval(image: Image, *args) -> Image: ...
def merge(mode: _Mode, bands: Sequence[Image]) -> Image: ...
def register_open(id: str, factory, accept=None) -> None: ...
def register_mime(id: str, mimetype: str) -> None: ...
def register_save(id: str, driver) -> None: ...
def register_save_all(id: str, driver) -> None: ...
def register_extension(id: str, extension: str) -> None: ...
def register_extensions(id: str, extensions: Iterable[str]) -> None: ...
def registered_extensions() -> dict[str, str]: ...
def register_decoder(name: str, decoder) -> None: ...
def register_encoder(name: str, encoder) -> None: ...
def effect_mandelbrot(size: tuple[int, int], extent: tuple[float, float, float, float], quality: int) -> Image: ...
def effect_noise(size: tuple[int, int], sigma: float) -> Image: ...
def linear_gradient(mode: _Mode) -> Image: ...
def radial_gradient(mode: _Mode) -> Image: ...

class Exif(MutableMapping[int, Any]):
    endian: Incomplete
    bigtiff: bool
    def load(self, data: bytes) -> None: ...
    def load_from_fp(self, fp, offset: Incomplete | None = None) -> None: ...
    def tobytes(self, offset: int = 8) -> bytes: ...
    def get_ifd(self, tag: int): ...
    def hide_offsets(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag: int) -> Any: ...
    def __contains__(self, tag: object) -> bool: ...
    def __setitem__(self, tag: int, value: Any) -> None: ...
    def __delitem__(self, tag: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
