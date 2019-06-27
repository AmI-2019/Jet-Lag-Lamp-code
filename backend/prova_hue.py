from hue import switch_on, switch_off, sun_set, sun_rise, mix_col



t=10

col = 0
color = mix_col(col)
switch_off()
#switch_on(5000, 50)
sun_rise(t,color)