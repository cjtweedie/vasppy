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
min1_k5_dos = Doscar("min1_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=min1_pos.get_chemical_symbols())
saddle_k5_dos = Doscar("saddle_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=saddle_pos.get_chemical_symbols())
pristine_k5_dos = Doscar("pristine_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
pristine_k5b_dos = Doscar("pristine_k5b_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
pristine_k5_lrealF_dos = Doscar("pristine_k5_lrealF_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
pristine_k7_dos = Doscar("pristine_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
pristine_k7b_dos = Doscar("pristine_k7b_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#print(min1_dos.species)
#min1_dos.pdos_sum()

# Cs doesn't contribute anything significant near Fermi level
# also Pb/I/Br s states further down in valence bulk states
# so can leave out if plotting close to E_F
orb_list_full = {'Cs': ['s','p'], 'Pb': ['s','p'], 'I': ['s','p'], 'Br': ['s','p']}
xrange_full = [-15,8]
xrange_EF = [-3,7]
xrange_half = [-7.5,7]
orb_list_EF = {'Pb': ['p'], 'I': ['p'], 'Br': ['p']}

# need to cat colour lists together if >10 orbitals (tableau list size 10 I think)
col = list(mcol.TABLEAU_COLORS) + list(mcol.TABLEAU_COLORS)
#assert isinstance(colors, Iterable)
#color_it = (c for c in colors)

fig1, ax1 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k5_dos.plot_pdos(ax=ax1, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig1.tight_layout()
fig1.savefig("pristine_k5_pdos.png")

fig2, ax2 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k5b_dos.plot_pdos(ax=ax2, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig2.tight_layout()
fig2.savefig("pristine_k5b_pdos.png")

fig3, ax3 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k5_lrealF_dos.plot_pdos(ax=ax3, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig3.tight_layout()
fig3.savefig("pristine_k5_lrealF_pdos.png")

fig4, ax4 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k7_dos.plot_pdos(ax=ax4, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig4.tight_layout()
fig4.savefig("pristine_k7_pdos.png")

fig5, ax5 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k7b_dos.plot_pdos(ax=ax5, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig5.tight_layout()
fig5.savefig("pristine_k7b_pdos.png")

fig6, ax6 = plt.subplots(1, 1, figsize=(8.0, 4.0))
min1_k5_dos.plot_pdos(ax=ax6, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig6.tight_layout()
fig6.savefig("min1_k5_pdos.png")

fig7, ax7 = plt.subplots(1, 1, figsize=(8.0, 4.0))
saddle_k5_dos.plot_pdos(ax=ax7, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=xrange_EF)
fig7.tight_layout()
fig7.savefig("saddle_k5_pdos.png")