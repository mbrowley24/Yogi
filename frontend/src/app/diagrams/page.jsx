"use client";

import ReactFlow, { Background, Controls, MiniMap, useNodesState, useEdgesState } from "reactflow";
import {useCallback} from "react";

const initialNodes = [
    { id: "1", position: { x: 0, y: 0 }, data: { label: "Firewall" } },
    { id: "2", position: { x: 220, y: 120 }, data: { label: "Switch" } },
];

const initialEdges = [{ id: "e1-2", source: "1", target: "2" }];

export default function DiagramsPage() {
    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
    const [edges, setEdges, onEdgeChange] = useEdgesState(initialEdges);

    const onConnect = useCallback(
        (params) => setEdges((eds) => [...eds, {...params, id: crypto.randomUUID()}]),
        [setEdges]
    )

    return (
        <div style={{ width: "100%", height: "80vh" }}>
            <ReactFlow
                nodes={nodes}
                edges={edges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgeChange}
                onConnect={onConnect}
                fitView
            >
                <Background />
                <MiniMap />
                <Controls />
            </ReactFlow>
        </div>
    );
}
