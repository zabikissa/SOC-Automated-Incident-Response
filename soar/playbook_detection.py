import phantom.rules as phantom

@phantom.playbook_block()
def on_start(container):
    phantom.debug("Début playbook SOC - Détection malware")
    file_reputation(container=container)
    return

@phantom.playbook_block()
def file_reputation(container):
    # Récupérer les hash depuis les artefacts
    container_artifacts = phantom.collect2(
        container=container,
        datapath=["artifact:*.cef.fileHash", "artifact:*.id"]
    )

    parameters = []
    for artifact in container_artifacts:
        if artifact[0] is not None:
            parameters.append({
                "hash": artifact[0],
                "context": {"artifact_id": artifact[1]},
            })

    # Appel VirusTotal
    phantom.act(
        "file reputation",
        parameters=parameters,
        name="check_virustotal",
        assets=["virustotal3"],
        callback=phantom.debug  # ici juste pour log, tu peux mettre un autre bloc
    )
    return
