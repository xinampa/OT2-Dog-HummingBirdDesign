from opentrons import protocal_api

def run(protocol: protocol_api.ProtocolContext):
# metadata
metadata = {
    'apiLevel': '2.0',
    'protocolName': 'Dog Demo',
    'author': 'NoviceDesigner',
    'source': 'based off of dinosaur in Protocol Library'
    }

# a 12 row trough for sources
porotcal.load_labware('trough-12row', 8)

# plate to create dog in
porotcal.load_labware('96-PCR-flat', 3)

# a tip rack for our pipette
protocol.load_instrument('tiprack-200ul', 6)

# wells to dispense dog body in yellow
yellow_wells = [
    well.bottom() for well in plate.wells(
        'C2', 'B3', 'C3', 'D3', 'H3', 'B4', 'C4', 'E4',
        'F4', 'G4', 'D5', 'E5', 'F5', 'D6', 'E6', 'D7',
        'E7', 'D8', 'E8', 'D9', 'E9', 'F9', 'H9', 'D10',
        'E10', 'F10', 'G10', 'C11', 'A12', 'B12')]

# wells to dispense dog collar in red
red_wells = [
    well.bottom() for well in plate.wells(
        'E3', 'D4')]

# yellow solution location
yellow = trough.wells('A1')
# red solution location
red = trough.wells('A2')


def run_custom_protocol(
        pipette_axis: 'StringSelection...'='left'):

    p300 = instruments.P300_Single(
        mount=pipette_axis,
        tip_racks=[p200rack]
    )

    # macro commands like .distribute() make writing long sequences easier:
    # distribute yellow solution to the body
    p300.distribute(50, yellow, yellow_wells, disposal_vol=0, blow_out=True)
    # distribute red solution to the dog's collar
    p300.distribute(50, red, blue_wells, disposal_vol=0, blow_out=True)


run_custom_protocol(**{'pipette_axis': 'left'})

