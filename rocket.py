import numpy as np
import itertools as it
import pandas as pd


def calc_prop(m_inert, m_payload, mass_ratio):
    m_prop = (m_inert + m_payload) * (mass_ratio - 1)
    return m_prop


def calc_inert(m_prop, inert_mass_frac):
    m_inert = m_prop / (1 - inert_mass_frac)
    return m_inert


# Replace iterative convergence with explicit equations (it's all IMF sizing for now)
@np.vectorize
def converge(delta_v, m_payload, inert_mass_frac, specific_impulse):
    mass_ratio = np.exp(delta_v / 9.80665 / specific_impulse)
    err = 100
    m_inert_guess = 1000.
    while err > 1:
        m_prop = calc_prop(m_inert_guess, m_payload, mass_ratio)
        m_inert_actual = calc_inert(m_prop, inert_mass_frac)
        err = np.abs(m_inert_actual - m_inert_guess)
        m_inert_guess = m_inert_actual
    m_inert = m_inert_actual
    return m_inert, m_prop


if __name__ == '__main__':
    delta_v_range = np.arange(2000, 2005, 5)
    # print(delta_v_range[0:5])
    imf_range = np.arange(0.15, 0.16, 0.01)
    # print(imf_range[0:5])
    m_payload_range = np.arange(3000, 3010, 10)
    # print(m_payload_range[0:5])
    a = it.product(*[delta_v_range, imf_range, m_payload_range])
    df = pd.DataFrame(list(a), columns=['Delta V (m/s)', 'IMF', 'Payload Mass (kg)'])
    df['Isp (s)'] = 325
    df['Inert Mass (kg)'], df['Propellant Mass (kg)'] = converge(df['Delta V (m/s)'], df['Payload Mass (kg)'],
                                                                 df['IMF'], df['Isp (s)'])
    print(df.head())
