import make_absolute_top_solvent as so
import argparse

parser = argparse.ArgumentParser(description='Deep DILI')
parser.add_argument(
        '--data_path', 
        default='.',
        type=str, help='Data directory')
parser.add_argument(
        '--compound_list', 
        default='.',
        type=str, help='List of ligands. Seperated by comma (ex: A,B,C)')
parser.add_argument(
        '--lig_name', 
        default='UNK',
        type=str, help='ligand name')
args = parser.parse_args()

#Name of project directory
dir = args.data_path
#List of ligands
compounds = list(args.compound_list.str.split(','))
#Three letter code ligands
lig = args.lig_name

for f in compounds:
    path = '%s/%s' % (dir,f)
    #specify output file name
    top = '%s/solvent.top'%path
    #Add dummy B state to the topology file
    so.create_top(top, top, 'vdwq_dummy', ligand=lig)