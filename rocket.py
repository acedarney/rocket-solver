import numpy as np
import itertools as it
import pandas as pd
from numba import vectorize, float64
from time import time


@vectorize([float64(float64, float64, float64)])
def calc_prop(m_payload, mass_ratio, inert_mass_frac):
    m_prop = m_payload * (mass_ratio - 1) * (1 - inert_mass_frac) / (1 - mass_ratio * inert_mass_frac)
    return m_prop


@vectorize([float64(float64, float64, float64)])
def calc_inert(m_payload, mass_ratio, inert_mass_frac):
    m_inert = m_payload * (mass_ratio - 1) * inert_mass_frac / (1 - mass_ratio * inert_mass_frac)
    return m_inert


if __name__ == '__main__':
    tic = time()
    delta_v_range = np.arange(2000, 3005, 5)
    # print(delta_v_range[0:5])
    imf_range = np.arange(0.15, 0.26, 0.01)
    # print(imf_range[0:5])
    m_payload_range = np.arange(3000, 4010, 10)
    # print(m_payload_range[0:5])
    a = it.product(*[delta_v_range, imf_range, m_payload_range])
    df = pd.DataFrame(list(a), columns=['Delta V (m/s)', 'IMF', 'Payload Mass (kg)'])
    df['Isp (s)'] = 325
    df['Mass Ratio'] = np.exp(df['Delta V (m/s)'] / 9.80665 / df['Isp (s)'])
    df['Inert Mass (kg)'] = calc_inert(df['Payload Mass (kg)'], df['Mass Ratio'], df['IMF'])
    df['Propellant Mass (kg)'] = calc_prop(df['Payload Mass (kg)'], df['Mass Ratio'], df['IMF'])
    df.to_csv('propulsive_stage_data.csv')
    toc = time()
    print('Elapsed Time: {}'.format(toc - tic))
    print(df.head())
