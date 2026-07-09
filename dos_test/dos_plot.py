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
saddle_pos = read("saddle_POSCAR")
pristine_pos = read("pristine_POSCAR")
#print(min1_pos.get_chemical_symbols())
min1_k5_dos = Doscar("min1_l5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=min1_pos.get_chemical_symbols())
saddle_k5_dos = Doscar("saddle_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=saddle_pos.get_chemical_symbols())
pristine_k5_dos = Doscar("pristine_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#print(min1_dos.species)
#min1_dos.pdos_sum()

# Cs doesn't contribute anything significant near Fermi level
# also Pb/I/Br s states further down in valence bulk states
# so can leave out if plotting close to E_F
orb_list_full = {'Cs': ['s','p'], 'Pb': ['s','p'], 'I': ['s','p'], 'Br': ['s','p']}
orb_list_EF = {'Pb': ['p'], 'I': ['p'], 'Br': ['p']}

# need to cat colour lists together if >10 orbitals (tableau list size 10 I think)
col = list(mcol.TABLEAU_COLORS) + list(mcol.TABLEAU_COLORS)
#assert isinstance(colors, Iterable)
#color_it = (c for c in colors)

fig1, ax1 = plt.subplots(1, 1, figsize=(10.5, 4.0))
min1_k5_dos.plot_pdos(ax=ax1, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=[-3,7])
fig1.savefig("min1_k5_pdos.png")

fig2, ax2 = plt.subplots(1, 1, figsize=(10.5, 4.0))
saddle_k5_dos.plot_pdos(ax=ax2, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=[-3,7])
fig2.savefig("saddle_k5_pdos.png")

fig3, ax3 = plt.subplots(1, 1, figsize=(10.5, 4.0))
pristine_k5_dos.plot_pdos(ax=ax3, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=[-3,7])
fig3.savefig("pristine_k5_pdos.png")