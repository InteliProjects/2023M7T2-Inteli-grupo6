'use client'
import React from "react";
import { Card } from "../Card";
import {
    Bar,
    BarChart,
    CartesianGrid,
    Legend,
    Line,
    LineChart,
    ResponsiveContainer,
    Tooltip,
    XAxis,
    YAxis,
} from "recharts";

export const FlightCharts = ({ flights }) => {
    const lineChartData = flights.map(({ name, createdAt, predictionResult }) => ({
        name,
        date: new Date(createdAt).toLocaleDateString(),
        predictionResult,
    }));

    const aggregatedData = flights.reduce((acc, { user }) => {
        if (!acc[user.name]) {
            acc[user.name] = { name: user.name, count: 0 };
        }
        acc[user.name].count++;
        return acc;
    }, {});

    const barChartData = Object.values(aggregatedData);

    return (
        <div className="flex gap-8 mb-8 w-full">
            <Card className="w-1/2">
                <h2 className="text-2xl text-primary mb-6 block">Histórico de Previsões por tempo</h2>
                <ResponsiveContainer width="100%" height={400}>
                    <LineChart data={lineChartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                        <XAxis dataKey="date" />
                        <YAxis />
                        <CartesianGrid strokeDasharray="3 3" />
                        <Tooltip />
                        <Line type="monotone" dataKey="predictionResult" stroke="#00a0e6" />
                    </LineChart>
                </ResponsiveContainer>
            </Card>
            <Card className="w-1/2">
                <h2 className="text-2xl text-primary mb-6 block">Distribuição de Previsões por Usuário</h2>
                <ResponsiveContainer width="100%" height={400}>
                    <BarChart data={barChartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                        <XAxis dataKey="name" />
                        <YAxis />
                        <CartesianGrid strokeDasharray="3 3" />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="count" fill="#00a0e6" />
                    </BarChart>
                </ResponsiveContainer>
            </Card>
        </div>
    );
};
