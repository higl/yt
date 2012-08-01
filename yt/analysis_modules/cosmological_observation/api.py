"""
API for cosmology analysis.

Author: Britton Smith <brittonsmith@gmail.com>
Affiliation: Michigan State University
Homepage: http://yt-project.org/
License:
  Copyright (C) 2010-2011 Matthew Turk.  All Rights Reserved.

  This file is part of yt.

  yt is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from .cosmology_splice import \
    CosmologySplice

from .light_cone.api import \
    LightCone, \
    find_unique_solutions, \
    project_unique_light_cones

from .light_ray.api import \
    LightRay