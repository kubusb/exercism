class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)

    if records[0].record_id != 0:
        raise ValueError("Record id is invalid or out of order.")

    record_ids = [record.record_id for record in records]
    for i in range(len(records)):
        if i not in record_ids:
            raise ValueError("Record id is invalid or out of order.")

    nodes = {}
    for record in records:
        if record.record_id in nodes:
            raise ValueError(f"Duplicate record ID {record.record_id} found.")
        nodes[record.record_id] = Node(record.record_id)

    for record in records:
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if record.parent_id not in nodes:
            raise ValueError("Parent id is invalid or out of order.")
        if record.record_id not in nodes:
            raise ValueError("Record id is invalid or out of order.")

        if record.record_id != 0:
            parent_node = nodes[record.parent_id]
            parent_node.children.append(nodes[record.record_id])

    return nodes[0]
