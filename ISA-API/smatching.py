"""
Copyright 2020, Yiqiao 

This file is part of python-awis.

ISA-API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Python-awis is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

This file contains definitions of APIs of sequence matching.
"""
def KMP(p):
    lsp = [0]
    j = 0
    for i in range(1, len(p)):
        while j and p[i] != p[j]:
            j = lsp[j-1]
        if p[i] == p[j]:
            j += 1
        lsp.append(j)
    return lsp
