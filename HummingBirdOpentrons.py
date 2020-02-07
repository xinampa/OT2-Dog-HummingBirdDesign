from opentrons import protocal_api

def run(protocol: protocol_api.ProtocolContext):

metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Hummingbird Demo',
    'author': 'NoviceDesigner',
    'source': 'based off of dinosaur in Protocol Library'
    }

# a 12 row trough for sources
porotcal.load_labware('trough-12row', 8)

# plate to create hummingbird in
porotcal.load_labware('96-PCR-flat', 3)

# a tip rack for our pipette
protocol.load_instrument('tiprack-200ul', 6)

# wells to dispense hummingbird body in red
red_wells = [well.bottom() for well in plate.wells(
        'C1', 'G1', 'B2', 'C2', 'G2', 'H2', 'A3', 'B3',
        'C3', 'G3', 'A4', 'B4', 'C4', 'F4', 'G4', 'B5',
        'C5', 'D5', 'E5', 'F5', 'C6', 'D6', 'B7', 'C7',
        'B8', 'C8', 'D8', 'B9', 'D9', 'E9','B10', 'D10','E10', 'F10', 'B11', 'E11','F11', 'G11','B12')]

        # wells to dispense hummingbird belly in green
green_wells = [well.bottom() for well in plate.wells('E6', 'F6', 'D7', 'E7')]
