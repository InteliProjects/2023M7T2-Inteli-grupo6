"use client";
import { fetchInstance } from "@/config/fetch";
import { apiRoutes } from "@/config/routes";
import { Pencil, RefreshCcw } from "lucide-react";
import { MRT_ColumnDef, MaterialReactTable } from "material-react-table";
import React, { useMemo, useState } from "react";
import { toast } from "react-toastify";
import { Badge, BadgeType } from "../Badge";
import { UserEditModal } from "../UserEditModal";
import { BarLoader } from "react-spinners";

export interface User {
    id: string;
    email: string;
    password: string;
    name: string;
    roles: string[];
    approved: boolean;
    createdAt: Date;
}

interface UsersTableProps {
    users: User[];
}

export const UsersTable: React.FC<UsersTableProps> = ({ users: usersFromServer }) => {
    const [users, setUsers] = useState<User[]>(usersFromServer);
    const [selectedUser, setSelectedUser] = useState<User | undefined>(undefined); //this is the selected row, if you enable row selection
    const [showEditModal, setShowEditModal] = useState(false);
    const [loading, setLoading] = useState(false);

    const getUsers = async () => {
        setLoading(true);
        try {
            const res = await fetchInstance(apiRoutes.admin.usersAll, {
                headers: {
                    contentType: "application/json",
                },
                method: "GET",
            });

            setUsers(res);
        } catch (error) {
            toast.error("Erro ao carregar usuários.");
        }
        setLoading(false);
    };

    const handleEditUser = (user: User) => {
        setSelectedUser(user);
        setShowEditModal(true);
    };

    const closeModal = () => {
        setShowEditModal(false);
        setSelectedUser(undefined);
    };

    const columns = useMemo<MRT_ColumnDef<User>[]>(
        () => [
            {
                accessorKey: "name", //simple recommended way to define a column
                header: "Nome",
            },
            {
                accessorKey: "email", //simple recommended way to define a column
                header: "Email",
            },
            {
                accessorFn: (originalRow) => (
                    <Badge
                        text={originalRow.approved ? "Aprovado" : "Não aprovado"}
                        type={originalRow.approved ? BadgeType.Success : BadgeType.Error}
                    />
                ), //alternate way
                id: "approved", //id required if you use accessorFn instead of accessorKey
                header: "Status",
            },
            {
                accessorFn: (originalRow) => (
                    <div className="flex gap-2">
                        {originalRow.roles.sort().map((role) => (
                            <Badge key={role} text={role} type={BadgeType.Info} />
                        ))}
                    </div>
                ),
                accessorKey: "roles", //id required if you use accessorFn instead of accessorKey
                header: "Permissões",
            },
            {
                accessorFn: (originalRow) => (
                    <Pencil
                        size={20}
                        className="text-yellow-400 cursor-pointer hover:scale-105 transition-all"
                        onClick={() => handleEditUser(originalRow)}
                    />
                ), //alternate way
                id: "id", //id required if you use accessorFn instead of accessorKey
                header: "Ações",
            },
        ],
        []
    );

    return (
        <>
            {loading ? (
                <BarLoader width={"100%"} color="#00a0e6" />
            ) : (
                <>
                    <MaterialReactTable
                        columns={columns}
                        renderTopToolbarCustomActions={() => (
                            <RefreshCcw
                                className="m-2 cursor-pointer hover:scale-105 transition-all"
                                onClick={getUsers}
                            />
                        )}
                        data={users}
                        enableRowSelection={false}
                        enableSelectAll={false}
                        enableGlobalFilter={true}
                    />
                    {selectedUser && (
                        <UserEditModal
                            getUsers={getUsers}
                            user={selectedUser}
                            showModal={showEditModal}
                            closeModal={closeModal}
                        />
                    )}
                </>
            )}
        </>
    );
};
