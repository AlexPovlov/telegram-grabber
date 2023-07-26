<script setup lang="ts">
import {
  Postcard,
  Plus,
  Delete,
  View,
  Phone,
  Notebook,
  CircleCheckFilled,
  WarningFilled,
} from "@element-plus/icons-vue";
import { ref } from "vue";
import type { IAccount } from "~/interfaces/IAccount";
import * as api from "~/requests/accounts";
import { ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";
import { useProgress } from "~/composables/useProgress";

const router = useRouter();
const form = ref<{ phone: string }>({ phone: "" });
const accounts = ref<IAccount[]>([]);
const search = ref("");

getData();

async function getData() {
  const progress = useProgress();
  progress.emitStart();
  let { data } = await api.all();
  progress.emitEnd(async () => {
    accounts.value = data;
  });
}

async function deleteAccount(id?: number) {
  if (id) {
    await ElMessageBox.confirm("Удалить аккаунт?", "Внимание", {
      confirmButtonText: "Подтвердить",
      cancelButtonText: "Отмена",
      type: "error",
    });
    try {
      await api.logout(id);
      setTimeout(getData, 1000);
      ElMessage.success("Аккаунт успешно удален");
    } catch (error) {
      ElMessage.warning("Что-то пошло не так");
      console.error(error);
    }
  }
}

async function addAccount() {
  api.sendCode(form.value.phone);
  const tfa = await ElMessageBox.prompt("TFA (необязательно)", "Авторизация", {
    confirmButtonText: "Далее",
    cancelButtonText: "Отмена",
  });
  const code = await ElMessageBox.prompt("Введите код из СМС", "Авторизация", {
    confirmButtonText: "Подтвердить",
    cancelButtonText: "Отмена",
  });
  try {
    await api.auth(form.value.phone, code.value, tfa.value || "");
    ElMessage.success("Аккаунт успешно добавлен");
    getData();
    form.value.phone = "";
  } catch (error) {
    ElMessage.warning("Что-то пошло не так");
    console.error(error);
  }
}
</script>
<template>
  <div class="index-page">
    <h3>
      <el-icon><Postcard /></el-icon> Аккаунты
    </h3>
    <el-form label-position="top">
      <div class="row">
        <div class="col-12 col-md-4">
          <el-form-item label="Добавить аккаунт">
            <div class="d-flex">
              <el-input
                class="mr-2"
                placeholder="Номер телефона"
                v-model="form.phone"
              >
              </el-input>
              <el-button
                type="primary"
                :icon="Plus"
                @click="addAccount"
                :disabled="!form.phone"
              />
            </div>
          </el-form-item>
        </div>
      </div>
    </el-form>
    <div class="common-list" v-if="accounts.length">
      <h3>
        <el-icon><Notebook /></el-icon> Список добвленных
      </h3>
      <div class="row">
        <div class="col-12 col-md-6 col-lg-4">
          <el-input class="mb-4" placeholder="Поиск..." v-model="search">
          </el-input>
        </div>
      </div>
      <div class="row">
        <template v-for="item in accounts">
          <div
            class="col-12 col-md-6 col-lg-4 mb-4"
            v-if="item.phone.includes(search)"
          >
            <el-card class="common-list__item">
              <template #header>
                <div class="d-flex">
                  <el-button
                    @click="router.push(`/detail/${item.id}`)"
                    size="small"
                    :icon="View"
                    type="primary"
                  >
                    Простотр
                  </el-button>
                  <el-button
                    size="small"
                    type="warning"
                    :icon="Delete"
                    @click="deleteAccount(item.id)"
                  ></el-button>
                </div>
              </template>

              <div class="common-list__item-info">
                <el-tooltip
                  v-if="item.auth"
                  content="Авторизовано"
                  placement="top"
                >
                  <el-icon class="common-list__item-info-status success">
                    <CircleCheckFilled />
                  </el-icon>
                </el-tooltip>

                <el-tooltip v-else content="Не авторизовано" placement="top">
                  <el-icon class="common-list__item-info-status warning">
                    <WarningFilled />
                  </el-icon>
                </el-tooltip>

                <div class="common-list__item-info-phone">
                  <el-icon class="common-list__item-info-phone-icon">
                    <Phone />
                  </el-icon>
                  {{ item.phone }}
                </div>
              </div>
            </el-card>
          </div>
        </template>
      </div>
    </div>
    <el-empty v-else description="Нет добавленных" />
  </div>
</template>
