import React from 'react'
import { Control, Controller, FieldErrors } from 'react-hook-form'
import ReactSelect, { Props as SelectProps } from 'react-select'

interface OptionType {
    label: string
    value: string
}

interface SelectPropsExtended extends Omit<SelectProps<OptionType>, 'onChange'> {
    control: Control<any>
    name: string
    options: OptionType[]
    placeholder?: string
    isMulti?: boolean
    errors: FieldErrors<any>
}

const Select: React.FC<SelectPropsExtended> = ({
    control,
    errors,
    name,
    options,
    placeholder = 'Select an option...',
    isMulti = false,
    ...props
}) => {
    const error = errors[name]?.message as string
    return (
        <div>
            <Controller
                name={name}
                control={control}
                defaultValue={isMulti ? [] : options[0].value}
                render={({ field }) => (
                    <ReactSelect
                        {...field}
                        options={options}
                        isSearchable
                        isMulti={isMulti}
                        placeholder={placeholder}
                        value={
                            isMulti
                                ? options.filter((option) => field.value.includes(option.value))
                                : options.find((option) => option.value === field.value)
                        }
                        onChange={(selected) => {
                            if (isMulti) {
                                const selectedValues = (selected as OptionType[]).map((option) => option.value)
                                field.onChange(selectedValues)
                            } else {
                                const selectedValue = (selected as OptionType).value
                                field.onChange(selectedValue)
                            }
                        }}
                        {...props}
                    />
                )}
            />
            {error && <span className="text-red-500 block mt-1 text-sm">{error}</span>}
        </div>
    )
}

export default Select
