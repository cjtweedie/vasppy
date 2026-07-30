from doscar import Doscar
#from procar import Procar
from ase import Atoms
from ase.io import read
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.colors as mcol
from collections.abc import Iterable

pristine_pos = read("pristine_POSCAR")
im00_pos = read("min1_POSCAR")
im01_pos = read("01_POSCAR")
im02_pos = read("saddle_POSCAR")
im03_pos = read("03_POSCAR")
im04_pos = read("min2_POSCAR")
#print(min1_pos.get_chemical_symbols())

#pristine_k5_dos = Doscar("pristine_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#pristine_k5b_dos = Doscar("pristine_k5b_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#pristine_k5_lrealF_dos = Doscar("pristine_k5_lrealF_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#pristine_k7_dos = Doscar("pristine_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
pristine_k7b_dos = Doscar("pristine_k7b_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=pristine_pos.get_chemical_symbols())
#min1_k5_dos = Doscar("min1_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im00_pos.get_chemical_symbols())
im00_k7_dos = Doscar("min1_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im00_pos.get_chemical_symbols())
im04_k7_dos = Doscar("min2_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im04_pos.get_chemical_symbols())
#saddle_k5_dos = Doscar("saddle_k5_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im02_pos.get_chemical_symbols())
im02_k7_dos = Doscar("saddle_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im02_pos.get_chemical_symbols())
im01_k7_dos = Doscar("01_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im01_pos.get_chemical_symbols())
im03_k7_dos = Doscar("03_k7_DOSCAR", ispin=1, lmax=2, lorbit=11, read_pdos=True, species=im03_pos.get_chemical_symbols())
#print(min1_dos.species)
#min1_dos.pdos_sum()

#print(im00_k7_dos.energy)
#print(im00_k7_dos.find_EF_range())

# Cs doesn't contribute anything significant near Fermi level
# also Pb/I/Br s states further down in valence bulk states
# so can leave out if plotting close to E_F
orb_list_full = {'Cs': ['s','p'], 'Pb': ['s','p'], 'I': ['s','p'], 'Br': ['s','p']}
orb_list_EF = {'Pb': ['p'], 'I': ['p'], 'Br': ['p']}
Erange_full = [-15, 8]
Erange_pristine_EF = [-2.37, 6.43]
Erange_VI0_EF = [-2.38, 6.32]
Erange_half = [-7.5, 7]
ymax_EF = 660

# need to cat colour lists together if >10 orbitals (tableau list size 10 I think)
col = list(mcol.TABLEAU_COLORS) + list(mcol.TABLEAU_COLORS)
#assert isinstance(colors, Iterable)
#color_it = (c for c in colors)

#fig1, ax1 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#pristine_k5_dos.plot_pdos(ax=ax1, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig1.tight_layout()
#fig1.savefig("pristine_k5_pdos.png")

#fig2, ax2 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#pristine_k5b_dos.plot_pdos(ax=ax2, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig2.tight_layout()
#fig2.savefig("pristine_k5b_pdos.png")

#fig3, ax3 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#pristine_k5_lrealF_dos.plot_pdos(ax=ax3, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig3.tight_layout()
#fig3.savefig("pristine_k5_lrealF_pdos.png")

#fig4, ax4 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#pristine_k7_dos.plot_pdos(ax=ax4, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig4.tight_layout()
#fig4.savefig("pristine_k7_pdos.png")

fig5, ax5 = plt.subplots(1, 1, figsize=(8.0, 4.0))
pristine_k7b_dos.plot_pdos(ax=ax5, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=pristine_k7b_dos.find_EF_range(), ymax=ymax_EF)
fig5.tight_layout()
fig5.savefig("pristine_k7b_pdos.png")

#fig6, ax6 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#min1_k5_dos.plot_pdos(ax=ax6, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig6.tight_layout()
#fig6.savefig("min1_k5_pdos.png")

fig7, ax7 = plt.subplots(1, 1, figsize=(8.0, 4.0))
im00_k7_dos.plot_pdos(ax=ax7, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=im00_k7_dos.find_EF_range(), ymax=ymax_EF)
fig7.tight_layout()
fig7.savefig("min1_k7_pdos.png")

fig8, ax8 = plt.subplots(1, 1, figsize=(8.0, 4.0))
im04_k7_dos.plot_pdos(ax=ax8, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=im04_k7_dos.find_EF_range(), ymax=ymax_EF)
fig8.tight_layout()
fig8.savefig("min2_k7_pdos.png")

#fig9, ax9 = plt.subplots(1, 1, figsize=(8.0, 4.0))
#saddle_k5_dos.plot_pdos(ax=ax9, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=Erange_EF)
#fig9.tight_layout()
#fig9.savefig("saddle_k5_pdos.png")

fig10, ax10 = plt.subplots(1, 1, figsize=(8.0, 4.0))
im02_k7_dos.plot_pdos(ax=ax10, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=im02_k7_dos.find_EF_range(), ymax=ymax_EF)
fig10.tight_layout()
fig10.savefig("saddle_k7_pdos.png")

fig11, ax11 = plt.subplots(1, 1, figsize=(8.0, 4.0))
im01_k7_dos.plot_pdos(ax=ax11, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=im01_k7_dos.find_EF_range(), ymax=ymax_EF)
fig11.tight_layout()
fig11.savefig("im01_k7_pdos.png")

fig12, ax12 = plt.subplots(1, 1, figsize=(8.0, 4.0))
im03_k7_dos.plot_pdos(ax=ax12, colours=col, plot_total_dos=True, to_plot=orb_list_EF, xrange=im03_k7_dos.find_EF_range(), ymax=ymax_EF)
fig12.tight_layout()
fig12.savefig("im03_k7_pdos.png")