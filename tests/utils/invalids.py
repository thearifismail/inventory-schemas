INVALID_SYSTEM_PROFILES = (
    {"infrastructure_type": "x" * 101},
    {"infrastructure_vendor": "x" * 101},
    {"network_interfaces": [{"mac_address": "x" * 60}]},
    {"network_interfaces": [{"name": "x" * 51}]},
    {"network_interfaces": [{"state": "x" * 26}]},
    {"network_interfaces": [{"type": "x" * 19}]},
    {"disk_devices": [{"device": "x" * 2049}]},
    {"disk_devices": [{"label": "x" * 1025}]},
    {"disk_devices": [{"options": {"": "XXX"}}]},
    {"disk_devices": [{"mount_point": "x" * 2049}]},
    {"disk_devices": [{"type": "x" * 257}]},
    {"bios_vendor": "x" * 101},
    {"bios_version": "x" * 101},
    {"bios_release_date": "x" * 51},
    {"cpu_flags": ["x" * 31]},
    {"os_release": "x" * 101},
    {"os_kernel_version": "x" * 21},
    {"arch": "x" * 51},
    {"kernel_modules": ["x" * 256]},
    {"last_boot_time": ["x" * 51]},
    {"running_processes": ["x" * 1001]},
    {"subscription_status": ["x" * 101]},
    {"subscription_auto_attach": ["x" * 101]},
    {"cloud_provider": ["x" * 101]},
    {"yum_repos": [{"id": "x" * 257}]},
    {"yum_repos": [{"name": "x" * 1025}]},
    {"yum_repos": [{"base_url": "x" * 2049}]},
    {"dnf_modules": [{"name": "x" * 129}]},
    {"dnf_modules": [{"stream": "x" * 2049}]},
    {"installed_products": [{"name": "x" * 513}]},
    {"installed_products": [{"id": "x" * 65}]},
    {"installed_products": [{"status": "x" * 257}]},
    {"insights_client_version": "x" * 51},
    {"insights_egg_version": "x" * 51},
    {"captured_date": "x" * 33},
    {"installed_packages": ["x" * 513]},
    {"installed_services": ["x" * 513]},
    {"enabled_services": ["x" * 513]},
    {"sap_sids": ["XXXX"]},
    {"sap_sids": ["XX"]},
    {"sap_sids": ["123"]},
    {"sap_sids": ["abc"]},
    {"sap_sids": ["ABC", "ABC"]},
    {"sap_system": "x"},
    {"sap_instance_number": "300"},
    {"sap_version": "1.00.122.04.147857563665464"},
    {"tuned_profile": "x"*257},
    {"selinux_current_mode": "random"},
    {"selinux_config_file": "random"},
    {"owner_id": "x"*12},
    {"rhc_client_id": "x"*12},
    {"rhc_client_id": "plxi13y1-99ut-3rdf-bc10-84opf904lfad"},
    {"cpu_model": "x"*101},
    {"number_of_cpus": "35465"},
    {"number_of_sockets": "35465"},
    {"cores_per_socket": "35465"},
    {"system_memory_bytes": "35465"},
    {"network_interfaces": [{"ipv4_addresses": "123.456.789.012"}]},
    {"network_interfaces": [{"ipv6_addresses": "0123:4567:89ab:cdef:0123:4567:89ab:cdef"}]},
    {"network_interfaces": [{"mtu": "15"}]},
    {"rhsm": {"version": "x" * 300}},
    {"operating_system": {"major": "10"}},
    {"operating_system": {"minor": "5"}},
    {"operating_system": {"name": 'ABCD'}},
    {"katello_agent_running": "False"},
    {"satellite_managed": "True"},
    {"yum_repos": [{"gpgcheck": "True"}]},
    {"yum_repos": [{"enabled": "False"}]},
    {"installed_packages_delta": ["x" * 513]},
)
