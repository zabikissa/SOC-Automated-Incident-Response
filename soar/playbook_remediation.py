import phantom.rules as phantom

@phantom.playbook_block()
def on_start(container):
    phantom.debug("Début playbook SOC - Remédiation")
    remove_file(container=container)
    return

@phantom.playbook_block()
def remove_file(container):
    artifacts = phantom.collect2(container=container, datapath=["artifact:*.cef.filePath","artifact:*.cef.sourceHostName"])
    parameters = []
    for artifact in artifacts:
        file_path = artifact[0]
        host = artifact[1]
        if file_path and host:
            parameters.append({
                "ip_hostname": host,
                "command": f"rm -rf {file_path}"
            })

    phantom.act(
        "execute program",
        parameters=parameters,
        name="delete_infected_file",
        assets=["ssh"],
        callback=phantom.debug
    )
    return
