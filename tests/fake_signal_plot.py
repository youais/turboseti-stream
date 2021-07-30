from astropy import units as u
import matplotlib.pyplot as plt
import setigen as stg
from main import DopplerFinder
plt.switch_backend('TkAgg')
import matplotlib
print(matplotlib.get_backend())
# clancy = DopplerFinder(filename="CH0_TIMESTAMP", source_name="luyten", src_raj=7.456805, src_dej=5.225785,
#                        tstart=0, tsamp=1, f_start=0, f_stop=1, n_fine_chans=1, n_ints_in_file=16)
# clancy.find_ET(np.zeros((256)))
f_start = 3e9 #Hz
BW = 1000e3 #Hz
f_stop = f_start + BW
n_fine_chans = 1000e3
ntime = 64
# Create a fake signal
frame = stg.Frame(fchans=n_fine_chans*u.pixel,
                  tchans=ntime*u.pixel,
                  df=1*u.Hz,
                  dt=1*u.s,
                  fch1=f_start*u.Hz)
noise = frame.add_noise(x_mean=10, noise_type='chi2')
signal = frame.add_signal(stg.constant_path(f_start=frame.get_frequency(index=n_fine_chans/2),
                                            drift_rate=2*u.Hz/u.s),
                          stg.constant_t_profile(level=frame.get_intensity(snr=100)),
                          stg.gaussian_f_profile(width=5*u.Hz),
                          stg.constant_bp_profile(level=1))
plt.figure()
plt.imshow(frame.data, interpolation='nearest', aspect='auto')
plt.show()
