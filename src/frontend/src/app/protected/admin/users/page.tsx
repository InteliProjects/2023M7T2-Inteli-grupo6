import { PageHeader } from "@/components/PageHeader";
import { UsersTable } from "@/components/UsersTable";
import { fetchInstance } from "@/config/fetch";
import { apiRoutes } from "@/config/routes";

const getUsers = async () => {
    try {
        const data = await fetchInstance(apiRoutes.admin.usersAll, {
            cache: "no-cache",
        });

        return data;
    } catch (error) {
        return [];
    }
};

const AdminUsersPage = async () => {
    const users = await getUsers();

    return (
        <>
            <PageHeader title="Usuários" subtitle="Página para gerenciar os usuários do sistema" />
            <UsersTable users={users} />
        </>
    );
};
export default AdminUsersPage;
