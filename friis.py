import streamlit as st
#import matplotlib.pyplot as plt

# Wzór Friisa
def friis(d, f, gt, gr):
    """
    Oblicza zysk łączny dla dwóch anten w odległości d i częstotliwości f.
    gt - zysk anteny nadawczej
    gr - zysk anteny odbiorczej
    """
    c = 3e8
    wavelength = c/f
    gain = (4 * 3.1415 * d / wavelength) ** 2
    return gt * gr * gain

# Aplikacja Streamlit
st.title("Obliczanie mocy nadajnika")

# Dane wejściowe
d = st.number_input("Odległość między antenami (w metrach)", min_value=0.0, max_value=1000.0, value=200.0, step=1.0)
f = st.number_input("Częstotliwość nadawania (w MHz)", min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
gt = st.number_input("Zysk anteny nadawczej", min_value=0.0, max_value=1000.0, value=1.0, step=0.1)
gr = st.number_input("Zysk anteny odbiorczej", min_value=0.0, max_value=1000.0, value=1.0, step=0.1)

# Obliczanie mocy nadajnika
p_tx = friis(d, (f/100) * 1e6, gt, gr)
st.write("Moc nadajnika potrzebna do nadania sygnału na odległość", d, "metrów na częstotliwości", f, "MHz wynosi", round(p_tx, 3), "W.")

# Wykres zależności mocy od odległości
#distances = range(10, 1000, 10)
#powers = [friis(d, (f/100) * 1e6, gt, gr) for d in distances]
#fig, ax = plt.subplots()
#ax.plot(distances, powers)
#ax.set(xlabel='Odległość (m)', ylabel='Moc nadajnika (W)',
#       title='Zależność mocy nadajnika od odległości')
#ax.grid()
#st.pyplot(fig)

# Wykres zależności mocy od odległości
distances = range(10, 1000, 10)
powers = [friis(d, (f/100) * 1e6, gt, gr) for d in distances]
chart_data = {'Odległość (m)': distances, 'Moc nadajnika (W)': powers}
st.line_chart(chart_data)
