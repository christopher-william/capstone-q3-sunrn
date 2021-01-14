from app.models import Hsp, Energy_data, Panel_price, energy_data_model


def panel_costs(pow_pico, pow_panel, price_panel):
    pow_pico = pow_pico * 1000
    panel_set_price = ((pow_pico//pow_panel) + 1) * price_panel

    return panel_set_price


def inversor_selector(inversor_list):
    def sort_inversors(e):
        return e.price

    available_inversors = list(
        filter(lambda inversor: inversor.power/0.8 >= ppico, inversor_list))
    available_inversors.sort(key=sort_inversors)
    return available_inversors[0]
