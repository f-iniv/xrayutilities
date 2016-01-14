# This file is part of xrayutilities.
#
# xrayutilities is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2016 Dominik Kriegner <dominik.kriegner@gmail.com>
"""
simulation subpackage of xrayutilities.

This package provides possibilities to simulation X-ray diffraction and
reflectivity curves of thin film samples. It could be extended for more
general use in future if there is demand for that.
"""

from .smaterials import SMaterial, MaterialList
from .smaterials import Layer, LayerStack

from .models import Model, LayerModel
from .models import KinematicalModel
from .models import SpecularReflectivityModel
