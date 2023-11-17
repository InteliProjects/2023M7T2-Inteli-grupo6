import React from "react";
import { FieldErrors, UseFormRegister } from "react-hook-form";

interface CheckboxProps {
    name: string;
    label: string;
    register: any
    errors: FieldErrors<any>;
}

export const Checkbox: React.FC<CheckboxProps> = ({ label, name, register, errors }) => {
    const error = errors[name]?.message as string;
    return (
        <div className="flex gap-4 items-center">
            <label htmlFor={"check_" + name}>{label}:</label>
            <input type="checkbox" id={"check_" + name} {...register} />
            {error && <span className="text-red-500">{error}</span>}
        </div>
    );
};
