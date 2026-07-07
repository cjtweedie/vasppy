from doscar import Doscar
#from procar import Procar
from ase import Atoms
from ase.io import read
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.colors as mcol
from collections.abc import Iterable

#min1_pos = IStructure.from_file("POSCAR")
#min1_pos_species = min1_pos.species
min1_pos = read("min1_POSCAR")
pristine_pos = read("pristine_POSCAR")
#print(min1_pos.get_chemical_symbols())
min1_dos = Doscar("min1_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=min1_pos.get_chemical_symbols())
pristine_dos = Doscar("pristine_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=min1_pos.get_chemical_symbols())
#print(min1_dos.species)
#min1_dos.pdos_sum()

col = list(mcol.TABLEAU_COLORS) + list(mcol.TABLEAU_COLORS)
#assert isinstance(colors, Iterable)
#color_it = (c for c in colors)
fig1, ax1 = plt.subplots(1, 1, figsize=(10.0, 4.0))
# Cs probably doesn't contribute anything significant near Fermi level
orb_list = {'Pb': ['s','p'], 'I': ['s','p'], 'Br': ['s','p']}
min1_dos.plot_pdos(ax=ax1, colours=col, plot_total_dos=True, to_plot=orb_list, xrange=[-15,5])
fig1.savefig("min1_pdos.png")

fig2, ax2 = plt.subplots(1, 1, figsize=(10.0, 4.0))
# Cs probably doesn't contribute anything significant near Fermi level
pristine_dos.plot_pdos(ax=ax2, colours=col, plot_total_dos=True, to_plot=orb_list, xrange=[-15,5])
fig2.savefig("pristine_pdos.png")