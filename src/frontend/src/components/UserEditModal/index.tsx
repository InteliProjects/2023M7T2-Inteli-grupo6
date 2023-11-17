import Modal from '@/components/Modal'
import { fetchInstance } from '@/config/fetch'
import { apiRoutes } from '@/config/routes'
import { yupResolver } from '@hookform/resolvers/yup'
import React from 'react'
import { useForm } from 'react-hook-form'
import { toast } from 'react-toastify'
import * as yup from 'yup'
import { Button } from '../Button'
import { Checkbox } from '../Checkbox'
import { User } from '../UsersTable'
import Select from '../Select'
import { BarLoader } from 'react-spinners'

enum Roles {
    ADMIN = 'ADMIN',
    USER = 'USER',
}

const schema = yup
    .object({
        approved: yup.boolean().required('Esse campo é obrigatório.'),
        roles: yup
            .array()
            .of(yup.string().oneOf([Roles.ADMIN, Roles.USER]))
            .min(1, 'Esse campo não pode estar vazio.')
            .required('Esse campo é obrigatório.'),
    })
    .required()

interface Props {
    showModal: boolean
    closeModal: () => void
    user: User
    getUsers: () => Promise<void>
}

export const UserEditModal: React.FC<Props> = ({ user, showModal, closeModal, getUsers }) => {
    const [loading, setLoading] = React.useState(false)
    const {
        register,
        handleSubmit,
        reset,
        control,
        formState: { errors },
        watch,
    } = useForm<any>({
        resolver: yupResolver(schema),
        defaultValues: { approved: user.approved, roles: user.roles },
    })

    const onSubmit = async (data: any) => {
        setLoading(true)
        try {
            await fetchInstance(apiRoutes.admin.userEdit(user?.id as string), {
                method: 'PATCH',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
            })

            toast.success('Usuário editado com sucesso.')
            await getUsers()
            setLoading(false)
            closeModal()
            reset()
        } catch (err) {
            setLoading(false)
            toast.error('Erro ao editar usuário.')
        }
    }

    const selectOptions = [
        { value: Roles.ADMIN, label: 'Administrador' },
        { value: Roles.USER, label: 'Usuário' },
    ]

    return (
        <Modal showModal={showModal} title="Editar usuário" closeModal={closeModal}>
            <form className="flex flex-col gap-4" onSubmit={handleSubmit(onSubmit)}>
                <Checkbox label="Aprovado" name="approved" register={{ ...register('approved') }} errors={errors} />
                <Select errors={errors} control={control} name="roles" options={selectOptions} isMulti />
                {loading ? <BarLoader width={'100%'} color="#00a0e6" /> : <Button>Editar</Button>}
            </form>
        </Modal>
    )
}
