import pytest
from mock import MagicMock

from cpu import CPU
from instructions import Sei, Cld
from instructions.store_instructions import StaAbs
from ppu import PPU
from ram import RAM


@pytest.fixture
def cpu():
    ram = RAM()
    ppu = PPU()
    cpu = CPU(ram, ppu)
    cpu.start_up()
    # Make mock-up ROM
    cpu.rom = MagicMock()
    cpu.rom.memory_start_location = 0
    cpu.rom.memory_end_location = 0x1FFF
    return cpu


def check_instruction_bytes(instruction, instruction_bytes):
    assert instruction.identifier_byte == instruction_bytes[0:1]


def get_data_bytes(instruction_bytes):
    return instruction_bytes[1:]


def test_lda_imm(cpu):
    instruction_bytes = bytes([0xA9, 0x10])
    instruction = LdaImmInstruction()

    check_instruction_bytes(instruction, instruction_bytes)
    # check that value has been loaded into a reg
    assert cpu.a_reg == 0
    instruction.execute(cpu, get_data_bytes(instruction_bytes))
    assert cpu.a_reg == get_data_bytes(instruction_bytes)[0]


def test_sta_abs(cpu):
    instruction_bytes = bytes([0x8D, 0x00, 0x20])
    instruction = StaAbs()

    check_instruction_bytes(instruction, instruction_bytes)
    # check that value in a reg has been loaded into memory
    # Set value in the CPU's A reg
    value_to_store = 8
    cpu.a_reg = value_to_store
    instruction.execute(cpu, get_data_bytes(instruction_bytes))

    # 0x00 0x20 -> $2000 -> 8192
    memory_location = 8192
    value_at_memory_location = cpu._get_memory_owner(memory_location).get(memory_location)
    assert value_at_memory_location == value_to_store


def test_sei(cpu):
    instruction_bytes = bytes([0x78])
    instruction = Sei()

    check_instruction_bytes(instruction, instruction_bytes)
    # check that the interrupt bit has been enabled
    cpu.status_reg.interrupt_bit = False
    instruction.execute(cpu, get_data_bytes(instruction_bytes))
    assert cpu.status_reg.interrupt_bit is True


def test_cld(cpu):
    instruction_bytes = bytes([0xD8])
    instruction = Cld()

    check_instruction_bytes(instruction, instruction_bytes)
    # check that the interrupt bit has been enabled
    cpu.status_reg.decimal_bit = True
    instruction.execute(cpu, get_data_bytes(instruction_bytes))
    assert cpu.status_reg.decimal_bit is False

