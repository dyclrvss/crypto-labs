from pyenigma import enigma
from pyenigma import rotor

def main():
    key = "AAA-AAA"
    ref = "B"
    r1 = "I"
    r2 = "II"
    r3 = "III"
    plugs = ""
    message = input("Enter your message: ").upper()

    rotors = {
        "I": rotor.ROTOR_I,
        "II": rotor.ROTOR_II,
        "III": rotor.ROTOR_III,
        "IV": rotor.ROTOR_IV,
        "V": rotor.ROTOR_V,
        "VI": rotor.ROTOR_VI,
        "VII": rotor.ROTOR_VII,
    }
    reflectors = {
        "A": rotor.ROTOR_Reflector_A,
        "B": rotor.ROTOR_Reflector_B,
        "C": rotor.ROTOR_Reflector_C,
    }

    if len(key) == 3:  
        key += "-AAA"

    engr = enigma.Enigma(
        reflectors[ref],
        rotors[r1],
        rotors[r2],
        rotors[r3],
        key=key[:3],
        plugs=plugs,
        ring=key[4:7],
    )
    res = engr.encipher(message).strip()
    print(res)

if __name__ == "__main__":
    main()
