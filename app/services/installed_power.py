from app.models import Hsp, Energy_data


def installed_power(db_hsp: Hsp, energy_data: Energy_data):

    hsp = db_hsp.md_anual/1000
    diary_energy = energy_data.month_energy/30
    ppico = diary_energy/hsp
    eficience = 1 - 0.2
    ppico_real = ppico/eficience

    return ppico
