import psutil
import GPUtil
import platform
import cpuinfo
import json


def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_list = []
    for gpu in gpus:
        gpu_info = {
            "vendor": gpu.name.split()[0],
            "model": gpu.name,
            "vram": gpu.memoryTotal,
            "utilization": gpu.load,
            "temperature": gpu.temperature,
        }
        gpu_list.append(gpu_info)
    return gpu_list


def get_cpu_info():
    cpu_info = cpuinfo.get_cpu_info()
    vendor = cpu_info["vendor_id_raw"]

    return {
        "vendor": "Intel" if vendor == "GenuineIntel" else "AMD",
        "model": cpu_info["brand_raw"],
        "threads": psutil.cpu_count(logical=True),
        "architecture": cpu_info["arch"],
        "utilization": psutil.cpu_percent() / 100.0,
    }


def get_ram_info():
    memory = psutil.virtual_memory()
    return {"installed": memory.total // (1024**2), "inUse": memory.used // (1024**2)}


def get_software_info():
    return {
        "os": platform.system(),
        "osVersion": platform.version(),
        "pythonVersion": platform.python_version(),
    }


def get_system_info():
    return {
        "gpu": get_gpu_info(),
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "software": get_software_info(),
    }
