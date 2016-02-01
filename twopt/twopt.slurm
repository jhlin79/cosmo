#!/bin/bash -l
#SBATCH -p regular
#SBATCH -N 64
#SBATCH -t 00:30:00
#SBATCH -J corr_north
#SBATCH -e twopt.error
#SBATCH -o twopt.out


cd $SLURM_SUBMIT_DIR

module load gsl

srun -n 64 -c 24 /project/projectdirs/boss/npadmana/twopt/./do_smu.x /global/homes/c/chienhao/cosmo/twopt/twopt.ini
