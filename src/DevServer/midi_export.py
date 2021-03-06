import midi
# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern(format=0, resolution=480)
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Midi Events Start Here
# Instantiate a MIDI note on event, append it to the track

time = midi.TimeSignatureEvent(tick=0, data = [4, 2, 24, 8])
track.append(time)
on = midi.NoteOnEvent(tick=0, velocity=83, pitch=midi.C_5)
track.append(on)
off = midi.NoteOffEvent(tick=132, velocity=0, pitch=midi.C_5)
track.append(off)
on = midi.NoteOnEvent(tick=588, velocity=55, pitch=midi.F_4)
track.append(on)
off = midi.NoteOffEvent(tick=63, velocity=0, pitch=midi.F_4)
track.append(off)
on = midi.NoteOnEvent(tick=177, velocity=60, pitch=midi.Gs_4)
track.append(on)
off = midi.NoteOffEvent(tick=426, velocity=0, pitch=midi.Gs_4)
track.append(off)
on = midi.NoteOnEvent(tick=294, velocity=55, pitch=midi.As_4)
track.append(on)
off = midi.NoteOffEvent(tick=99, velocity=0, pitch=midi.As_4)
track.append(off)
on = midi.NoteOnEvent(tick=141, velocity=67, pitch=midi.C_5)
track.append(on)
off = midi.NoteOffEvent(tick=131, velocity=0, pitch=midi.C_5)
track.append(off)
on = midi.NoteOnEvent(tick=349, velocity=74, pitch=midi.C_5)
track.append(on)
off = midi.NoteOffEvent(tick=122, velocity=0, pitch=midi.C_5)
track.append(off)
on = midi.NoteOnEvent(tick=358, velocity=58, pitch=midi.F_4)
track.append(on)
off = midi.NoteOffEvent(tick=80, velocity=0, pitch=midi.F_4)
track.append(off)
on = midi.NoteOnEvent(tick=160, velocity=56, pitch=midi.Gs_4)
track.append(on)
off = midi.NoteOffEvent(tick=366, velocity=0, pitch=midi.Gs_4)
track.append(off)
on = midi.NoteOnEvent(tick=114, velocity=57, pitch=midi.As_4)
track.append(on)
off = midi.NoteOffEvent(tick=158, velocity=0, pitch=midi.As_4)
track.append(off)
on = midi.NoteOnEvent(tick=82, velocity=53, pitch=midi.Gs_4)
track.append(on)
off = midi.NoteOffEvent(tick=105, velocity=0, pitch=midi.Gs_4)
track.append(off)
on = midi.NoteOnEvent(tick=135, velocity=71, pitch=midi.C_5)
track.append(on)
off = midi.NoteOffEvent(tick=167, velocity=0, pitch=midi.C_5)
track.append(off)
on = midi.NoteOnEvent(tick=553, velocity=49, pitch=midi.F_4)
track.append(on)
off = midi.NoteOffEvent(tick=126, velocity=0, pitch=midi.F_4)
track.append(off)
on = midi.NoteOnEvent(tick=114, velocity=50, pitch=midi.Gs_4)
track.append(on)
off = midi.NoteOffEvent(tick=478, velocity=0, pitch=midi.Gs_4)
track.append(off)
on = midi.NoteOnEvent(tick=2, velocity=55, pitch=midi.As_4)
track.append(on)
off = midi.NoteOffEvent(tick=65, velocity=0, pitch=midi.As_4)
track.append(off)
on = midi.NoteOnEvent(tick=175, velocity=47, pitch=midi.Ds_4)
track.append(on)
off = midi.NoteOffEvent(tick=153, velocity=0, pitch=midi.Ds_4)
track.append(off)
on = midi.NoteOnEvent(tick=327, velocity=53, pitch=midi.Ds_4)
track.append(on)
off = midi.NoteOffEvent(tick=220, velocity=0, pitch=midi.Ds_4)
track.append(off)
on = midi.NoteOnEvent(tick=260, velocity=57, pitch=midi.C_4)
track.append(on)
off = midi.NoteOffEvent(tick=225, velocity=0, pitch=midi.C_4)
track.append(off)
on = midi.NoteOnEvent(tick=255, velocity=56, pitch=midi.Ds_4)
track.append(on)
off = midi.NoteOffEvent(tick=406, velocity=0, pitch=midi.Ds_4)
track.append(off)


eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
#print pattern
midi.write_midifile("midi_export.mid", pattern)