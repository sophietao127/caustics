from collections import defaultdict
from typing import Any, Dict, Optional, Tuple

import torch
from torch import Tensor

from ..cosmology import Cosmology
from ..utils import translate_rotate
from .base import ThinLens

__all__ = ("Point",)


class Point(ThinLens):
    def __init__(
        self,
        name: str,
        cosmology: Cosmology,
        z_l: Optional[Tensor] = None,
        thx0: Optional[Tensor] = None,
        thy0: Optional[Tensor] = None,
        th_ein: Optional[Tensor] = None,
        s: Optional[Tensor] = torch.tensor(0.0),
    ):
        super().__init__(name, cosmology, z_l)

        self.add_param("thx0", thx0)
        self.add_param("thy0", thy0)
        self.add_param("th_ein", th_ein)
        self.add_param("s", s)

    def alpha(
        self,
        thx: Tensor,
        thy: Tensor,
        z_s: Tensor,
        x: Dict[str, Any] = defaultdict(list),
    ) -> Tuple[Tensor, Tensor]:
        z_l, thx0, thy0, th_ein, s = self.unpack(x)

        thx, thy = translate_rotate(thx, thy, thx0, thy0)
        th = (thx**2 + thy**2).sqrt() + s
        ax = thx / th**2 * th_ein**2
        ay = thy / th**2 * th_ein**2
        return ax, ay

    def Psi(
        self,
        thx: Tensor,
        thy: Tensor,
        z_s: Tensor,
        x: Dict[str, Any] = defaultdict(list),
    ) -> Tensor:
        z_l, thx0, thy0, th_ein, s = self.unpack(x)

        thx, thy = translate_rotate(thx, thy, thx0, thy0)
        th = (thx**2 + thy**2).sqrt() + s
        return th_ein**2 * th.log()

    def kappa(
        self,
        thx: Tensor,
        thy: Tensor,
        z_s: Tensor,
        x: Dict[str, Any] = defaultdict(list),
    ) -> Tensor:
        z_l, thx0, thy0, th_ein, s = self.unpack(x)

        thx, thy = translate_rotate(thx, thy, thx0, thy0)
        return torch.where((thx == 0) & (thy == 0), torch.inf, 0.0)
