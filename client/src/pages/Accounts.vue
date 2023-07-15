<script setup lang="ts">
import {
  Postcard,
  Plus,
  Delete,
  ChatDotSquare,
  Phone,
  Notebook,
} from "@element-plus/icons-vue";
import { reactive, ref } from "vue";
import { vMaska, type MaskaDetail } from "maska";
import { displayPhone } from "~/utils/phone";
import type { IAccount } from "~/interfaces/IAccount";
import * as api from "~/requests/accounts";
import { ElMessage, ElMessageBox } from "element-plus";

const phoneMask = reactive<MaskaDetail>({
  masked: "",
  unmasked: "",
  completed: false,
});

const form = ref<{ phone: string }>({ phone: "" });
const accounts = ref<IAccount[]>([]);
const search = ref("");

getData()

async function getData() {
  let { data } = await api.all();
  accounts.value = data;
}

async function addAccount() {
  try {
    const phone = phoneMask.unmasked;
    api.sendCode(phone);
    let code = await ElMessageBox.prompt("Введите код из СМС", "Авторизация", {
      confirmButtonText: "Подтвердить",
      cancelButtonText: "Отмена",
    });
    await api.auth(phone, code.value);
    form.value.phone = "";
    getData()
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
      <p></p>
      <div class="row">
        <div class="col-12 col-md-4">
          <el-form-item label="Добавить аккаунт">
            <div class="d-flex">
              <el-input
                class="mr-2"
                v-maska="phoneMask"
                data-maska="+# (###) ### ## ##"
                placeholder="Номер телефона"
                v-model="form.phone"
              >
              </el-input>
              <el-button type="primary" :icon="Plus" @click="addAccount" />
            </div>
          </el-form-item>
        </div>
      </div>
    </el-form>
    <div class="accounts-list" v-if="accounts.length">
      <h3>
        <el-icon><Notebook /></el-icon> Список добвленных
      </h3>
      <div class="row">
        <div class="col-12 col-md-6 col-lg-4">
          <el-input
            v-maska
            data-maska="+# (###) ### ## ##"
            class="mb-4"
            placeholder="Поиск..."
            v-model="search"
          >
          </el-input>
        </div>
      </div>
      <div class="row">
        <template v-for="item in accounts">
          <div
            class="col-12 col-md-6 col-lg-4 mb-4"
            v-if="displayPhone(item.phone).includes(search)"
          >
            <el-card>
              <template #header>
                <div class="d-flex justify-content-between">
                  <el-button size="small" :icon="ChatDotSquare" type="success">
                    Список чатов
                  </el-button>
                  <el-button
                    size="small"
                    type="warning"
                    :icon="Delete"
                  ></el-button>
                </div>
              </template>
              <div style="font-size: 14px">
                <el-icon><Phone /></el-icon> {{ displayPhone(item.phone) }}
              </div>
            </el-card>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>
