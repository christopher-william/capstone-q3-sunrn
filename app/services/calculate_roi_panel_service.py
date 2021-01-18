from app.models import Hsp, Energy_data, Panel_price, energy_data_model


def panel_set_costs(pow_pico, pow_panel, price_panel):
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


def panel_selector(panel_list, pow_pico):

    def sort_panel(e):
        return panel_set_costs(pow_pico, e.power, e.price)

    panel_list.sort(key=sort_panel)
    selected_panel = panel_list[0]
    selected_panel_quantity = pow_pico//selected_panel.power + 1

    return {
        "panel": selected_panel,
        "quantity": selected_panel_quantity
    }
