import React from "react";

export enum BadgeType {
    Success,
    Error,
    Info
}

interface BadgeProps {
    type: BadgeType;
    text: string;
}

const badgeColors = {
    base: "inline-block px-2 py-1 text-xs font-medium rounded",
    [BadgeType.Success]: "bg-green-400 text-green-800",
    [BadgeType.Error]: "bg-red-100 text-red-800",
    [BadgeType.Info]: "bg-blue-400 text-white",
};

export const Badge: React.FC<BadgeProps> = ({ text, type }) => {
    const badgeClassName = `${badgeColors.base} ${badgeColors[type]}`;

    return <div className={badgeClassName}>{text}</div>;
};
