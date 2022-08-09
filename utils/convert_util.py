def get_hardware_addr(hex: str):
    return bytes.fromhex(hex.replace(':', ''))

