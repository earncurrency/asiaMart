<template class="">
  <backend_navbar @showFormTable="showFormTable" />
  <Modal ref="modal" @showFormTable="showFormTable" />

  <div class="p-4 lg:pr-24 lg:pl-24 pt-6 sm:ml-64">
    <div
      class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-14"
    >
      <div class="mt-2 mb-2">
        <div class="lg:p-4 w-full rounded-md text-gray-600">
          <div v-if="formTable">
            <!-- title -->
            <div class="flex justify-between items-center mb-2">
              <p class="text-3xl font-semibold">รายการสินค้าเเนะนำ</p>
              <button
                @click="showFormAdd"
                class="block py-2 px-6 bg-green-500 hover:bg-green-600 text-white rounded-md transition"
              >
                <i class="fa-solid fa-plus"></i>
              </button>
            </div>

            <!-- sort -->
            <div class="lg:flex lg:justify-between mb-4 mt-4 items-center">
              <!-- ช่องค้นหา -->
              <div class="flex items-center w-1/4">
                <label for="voice-search" class="sr-only">Search</label>

                <div class="relative w-full">
                  <div
                    class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"
                  >
                    <i class="fa-solid fa-magnifying-glass"></i>
                  </div>
                  <input
                    type="text"
                    v-model="searchText"
                    @input="searchRecommend"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full pl-10 pr-10 p-2.5 focus:border-gray-300"
                    placeholder="ค้นหา..."
                  />

                  <button
                    @click="xmark"
                    class="absolute inset-y-0 end-0 flex items-center ps-3 p-3 pointer"
                  >
                    <i class="fa-solid fa-xmark"></i>
                  </button>
                </div>
              </div>

              <!-- เลือกสถานะ-->
              <div class="flex gap-2 justify-center pt-4 lg:pt-0">
                <div class="relative">
                  <!-- ปุ่มเลือกสถานะ-->
                  <button
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-16 p-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="clickDropdownStatus"
                  >
                    <span class="mr-2">
                      <span>สถานะ : {{ DropdownStatusName }}</span>
                    </span>
                    <i class="fa-solid fa-angle-down"></i>
                  </button>
                  <!-- เมนูสถานะ -->
                  <div
                    v-show="DropdownStatusOpen"
                    ref="statusMenu"
                    class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300"
                  >
                    <ul class="py-2">
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus('')"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >ทั้งหมด</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus('active', 'เเสดง')"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >เเสดง</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="DropdownStatus('inactive', 'ไม่เเสดง')"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >ไม่เเสดง</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- เลือกขนาดเเถวในตาราง -->
                <div class="relative">
                  <!-- ปุ่มเลือกขนาดเเถวในตาราง -->
                  <button
                    class="border border-gray-300 bg-gray-50 font-medium rounded-lg text-sm px-5 p-2.5 text-center inline-flex items-center h-full"
                    type="button"
                    @click="togglePageSize"
                  >
                    <span class="mr-2">{{ dataPaging.rows }}</span
                    ><i class="fa-solid fa-angle-down"></i>
                  </button>
                  <!-- เมนูขนาดเเถวในตาราง -->
                  <div
                    v-show="pageSizeOpen"
                    ref="pageSizeMenu"
                    class="z-50 absolute right-0 mt-2 text-base list-none w-full bg-white divide-y divide-gray-100 rounded-lg shadow border border-gray-300"
                  >
                    <ul class="py-2">
                      <li>
                        <a
                          href="#"
                          @click="pageSize(5)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >5</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(10)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >10</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(20)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >20</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(50)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >50</a
                        >
                      </li>
                      <li>
                        <a
                          href="#"
                          @click="pageSize(100)"
                          class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          >100</a
                        >
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- ตาราง -->
            <div
              class="relative overflow-x-auto rounded-lg border border-gray-200"
            >
              <table
                class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400"
              >
                <thead
                  class="text-sm text-gray-100 uppercase bg-gray-800 dark:bg-gray-700 dark:text-gray-400"
                >
                  <tr>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">รูป</th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      รหัส
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      ชื่อ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      เริ่มต้นเเนะนำ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      สิ้นสุด
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap">
                      สถานะ
                    </th>
                    <th scope="col" class="px-6 py-4 whitespace-nowrap"></th>
                  </tr>
                </thead>

                <tbody>
                  <tr
                    v-for="(recommend, index) in recommends"
                    :key="index"
                    @click="showFormEdit(recommend.id)"
                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 cursor-pointer hover:bg-gray-100 transition"
                  >
                    <th scope="row" class="px-6 py-4">
                      <div
                        v-if="
                          recommend.images.length > 0 && recommend.images[0]
                        "
                        class="w-24 h-24 lg:w-24 lg:h-24"
                      >
                        <img
                          class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                          :src="`${imageUrl}/api/uploads/${Math.ceil(
                            recommend.id / 100
                          )}/${recommend.images[0]}`"
                        />
                      </div>
                      <div v-else class="w-24 h-24 lg:w-24 lg:h-24">
                        <img
                          class="w-full h-full rounded-md object-cover ring-4 ring-gray-300 shadow-md"
                          :src="`${imageUrl}/src/assets/image/system/product.png`"
                        />
                      </div>
                    </th>

                    <td class="px-6 py-4 whitespace-nowrap font-semibold">
                      {{ recommend.code }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      {{ recommend.name }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      {{ recommend.start_date }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      {{ recommend.end_date }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        v-if="recommend.status === 'active'"
                        class="font-semibold text-green-500 p-1 bg-green-100 rounded-md"
                      >
                        แสดง
                      </span>
                      <span
                        v-else
                        class="font-semibold text-red-500 p-1 bg-red-100 rounded-md"
                      >
                        ไม่แสดง
                      </span>
                    </td>
                    <td class="px-6 py-4">
                      <button
                        @click.stop="btnDelete(recommend.id)"
                        class="bg-red-500 text-white px-4 py-2 rounded-md"
                      >
                        <i class="fa-solid fa-trash-can"></i>
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
              <pagination
                ref="paginationRef"
                :pageSize="dataPaging.rows"
                :totalList="totalList"
                @reloadData="reloadData"
              />
            </div>
          </div>

          <div v-if="formAdd">
            <!-- title -->
            <div class="flex gap-2 items-center mb-2">
              <p class="text-3xl font-semibold">เพิ่มสินค้าเเนะนำ</p>
            </div>

            <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="relative w-full lg:w-1/3">
                <input
                  type="text"
                  v-model="searchDataProduct"
                  @input="searchProduct"
                  class="block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300"
                  placeholder="ค้นหาสินค้า"
                  required
                />
                <div
                  class="absolute z-10 bg-white border border-gray-300 shadow-md rounded-lg w-full"
                  v-show="products.length > 0"
                >
                  <option
                    v-for="product in products"
                    :key="product.id"
                    @click="clickProduct(product)"
                    class="cursor-pointer p-2 bg-white hover:bg-gray-50 text-black border-gray-300 hover:border-gray-50 rounded-lg whitespace-nowrap overflow-hidden overflow-ellipsis"
                  >
                    {{ product.code }} {{ product.name }}
                  </option>
                </div>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <flat-pickr
                  v-model="recommend.start_date"
                  ref="inputStartDate"
                  :config="startDateConfig"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.start_date,
                  }"
                  placeholder="วันเริ่มต้น"
                  required
                />
                <i
                  class="fas fa-calendar-alt absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none"
                ></i>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <flat-pickr
                  v-model="recommend.end_date"
                  ref="inputEndDate"
                  :config="endDateConfig"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.end_date,
                  }"
                  placeholder="วันสิ้นสุด"
                  required
                />
                <i
                  class="fas fa-calendar-alt absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none"
                ></i>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <select
                  v-model="recommend.status"
                  ref="inputStatusRecommend"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.status,
                  }"
                  required
                >
                  <option value="" disabled selected>สถานะ</option>
                  <option value="active">เเสดง</option>
                  <option value="inactive">ไม่เเสดง</option>
                </select>
              </div>
            </div>

            <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="w-full lg:w-1/4">
                <input
                  type="text"
                  v-model="product.code"
                  ref="inputNameProduct"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !product.code,
                  }"
                  placeholder="รหัสสินค้า"
                  disabled
                />
              </div>
              <div class="w-full lg:w-3/4">
                <input
                  type="text"
                  v-model="product.name"
                  ref="inputNameProduct"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !product.name,
                  }"
                  placeholder="ชื่อสินค้า"
                  disabled
                />
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full">
                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="product.cost"
                    ref="inputCostProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.cost,
                    }"
                    placeholder="ราคาทุน"
                    @input="validateNumberInput"
                    disabled
                  />
                </div>

                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="product.price"
                    ref="inputPriceProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.price,
                    }"
                    placeholder="ราคาขาย"
                    @input="validateNumberInput"
                    disabled
                  />
                </div>
              </div>

              <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="product.category_id"
                    ref="inputTypeProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.category_id,
                    }"
                    disabled
                  >
                    <option value="" disabled selected>หมวดหมู่สินค้า</option>
                    <option v-for="category in categorys" :value="category.id">
                      {{ category.name }}
                    </option>
                  </select>
                </div>

                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="product.status"
                    ref="inputStatusProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.status,
                    }"
                    disabled
                  >
                    <option value="" disabled selected>สถานะ</option>
                    <option value="active">เเสดง</option>
                    <option value="inactive">ไม่เเสดง</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full">
                <div class="w-full">
                  <textarea
                    type="text"
                    v-model="product.detail"
                    ref="inputDetailProduct"
                    rows="4"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.detail,
                    }"
                    placeholder="รายละเอียดสินค้า"
                    disabled
                  />
                </div>
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-4 pt-1 mt-5">
              <!-- แสดงภาพของสินค้า -->
              <div
                v-if="product.images.length > 0"
                class="image-preview grid grid-cols-2 lg:grid-cols-5 gap-8"
              >
                <div
                  v-for="(image, imageIndex) in product.images"
                  :key="imageIndex"
                  class="preview-item relative"
                >
                  <!-- แทนที่ชื่อไฟล์ภาพด้วยตัวแปร image -->
                  <img
                    :src="`${imageUrl}/api/uploads/${Math.ceil(
                      product.id / 100
                    )}/${image}`"
                    alt="Product Image Preview"
                    class="w-32 h-32 lg:w-64 lg:h-48 object-cover rounded-md"
                  />
                </div>
              </div>
            </div>

            <hr class="my-2 text-gray-600" />

            <div class="flex gap-2 justify-center mt-4 md:mt-4">
              <button
                @click="btnAdd"
                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยืนยัน
              </button>
              <button
                @click="showFormTable"
                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยกเลิก
              </button>
            </div>
          </div>

          <!------------------------------------------------------------------>

          <div v-if="formEdit">
            <!-- title -->
            <div class="flex justify-between items-center mb-2">
              <p class="text-3xl font-semibold">เเก้ไขข้อมูลสินค้าเเนะนำ</p>
              <button
                @click.stop="btnDelete(recommend.id)"
                class="bg-red-500 text-white px-4 py-1.5 rounded-md"
              >
                <i class="fa-solid fa-trash-can"></i>
              </button>
            </div>

            <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="relative w-full lg:w-1/3">
                <input
                  type="text"
                  v-model="searchDataProduct"
                  @input="searchProduct"
                  class="block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300"
                  placeholder="ค้นหาสินค้า"
                  required
                />
                <div
                  class="absolute z-10 bg-white border border-gray-300 shadow-md rounded-lg w-full"
                  v-show="products.length > 0"
                >
                  <option
                    v-for="product in products"
                    :key="product.id"
                    @click="clickProduct(product)"
                    class="cursor-pointer p-2 bg-white hover:bg-gray-50 text-black border-gray-300 hover:border-gray-50 rounded-lg whitespace-nowrap overflow-hidden overflow-ellipsis"
                  >
                    {{ product.code }} {{ product.name }}
                  </option>
                </div>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <flat-pickr
                  v-model="recommend.start_date"
                  ref="inputStartDate"
                  :config="startDateConfig"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.start_date,
                  }"
                  placeholder="วันเริ่มต้น"
                  required
                />
                <i
                  class="fas fa-calendar-alt absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none"
                ></i>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <flat-pickr
                  v-model="recommend.end_date"
                  ref="inputEndDate"
                  :config="endDateConfig"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.end_date,
                  }"
                  placeholder="วันสิ้นสุด"
                  required
                />
                <i
                  class="fas fa-calendar-alt absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 pointer-events-none"
                ></i>
              </div>
              <div class="w-full lg:w-1/3 relative">
                <select
                  v-model="recommend.status"
                  ref="inputStatusRecommend"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-white h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !recommend.status,
                  }"
                  required
                >
                  <option value="" disabled selected>สถานะ</option>
                  <option value="active">เเสดง</option>
                  <option value="inactive">ไม่เเสดง</option>
                </select>
              </div>
            </div>

            <div class="flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="w-full lg:w-1/4">
                <input
                  type="text"
                  v-model="product.code"
                  ref="inputCodeProduct"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !product.code,
                  }"
                  placeholder="รหัสสินค้า"
                  disabled
                />
              </div>
              <div class="w-full lg:w-3/4">
                <input
                  type="text"
                  v-model="product.name"
                  ref="inputNameProduct"
                  :class="{
                    'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                    'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                      !product.name,
                  }"
                  placeholder="ใส่ชื่อสินค้า"
                  disabled
                />
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full">
                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="product.cost"
                    ref="inputCostProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.cost,
                    }"
                    placeholder="ราคาทุน"
                    @input="validateNumberInput"
                    disabled
                  />
                </div>

                <div class="lg:w-1/2 w-full">
                  <input
                    type="text"
                    v-model="product.price"
                    ref="inputPriceProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.price,
                    }"
                    placeholder="ราคาขาย"
                    @input="validateNumberInput"
                    disabled
                  />
                </div>
              </div>

              <div class="flex gap-2 w-full pt-1 mt-4 lg:pt-0 lg:mt-0">
                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="product.category_id"
                    ref="inputTypeProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.category_id,
                    }"
                    disabled
                  >
                    <option value="" disabled selected>หมวดหมู่สินค้า</option>
                    <option v-for="category in categorys" :value="category.id">
                      {{ category.name }}
                    </option>
                  </select>
                </div>

                <div class="lg:w-1/2 w-full">
                  <select
                    v-model="product.status"
                    ref="inputStatusProduct"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.status,
                    }"
                    disabled
                  >
                    <option value="" disabled selected>สถานะ</option>
                    <option value="active">เเสดง</option>
                    <option value="inactive">ไม่เเสดง</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-2 pt-1 mt-4">
              <div class="flex gap-2 w-full">
                <div class="w-full">
                  <textarea
                    type="text"
                    v-model="product.detail"
                    ref="inputDetailProduct"
                    rows="4"
                    :class="{
                      'block text-sm text-gray-900 border border-gray-300 rounded-lg w-full bg-gray-100 h-full p-2.5 focus:border-blue-300 focus:ring-2 focus:ring-blue-300': true,
                      'focus:border-blue-300 focus:ring-2 focus:ring-blue-300':
                        !product.detail,
                    }"
                    placeholder="รายละเอียดสินค้า"
                    disabled
                  />
                </div>
              </div>
            </div>

            <div class="md:flex w-full gap-2 mb-4 pt-1 mt-5">
              <!-- แสดงภาพของสินค้า -->
              <div
                v-if="product.images.length > 0"
                class="image-preview grid grid-cols-2 lg:grid-cols-5 gap-8"
              >
                <div
                  v-for="(image, imageIndex) in product.images"
                  :key="imageIndex"
                  class="preview-item relative"
                >
                  <!-- แทนที่ชื่อไฟล์ภาพด้วยตัวแปร image -->
                  <img
                    :src="`${imageUrl}/api/uploads/${Math.ceil(
                      product.id / 100
                    )}/${image}`"
                    alt="Product Image Preview"
                    class="w-32 h-32 lg:w-64 lg:h-48 object-cover rounded-md"
                  />
                </div>
              </div>
            </div>

            <hr class="my-2 text-gray-600" />

            <div class="flex gap-2 justify-center mt-4 md:mt-6">
              <button
                @click="btnEdit"
                class="text-white bg-blue-500 border border-blue-500 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยืนยัน
              </button>
              <button
                @click="showFormTable"
                class="text-black bg-gray-200 border border-gray-400 font-medium rounded-lg text-sm px-3 p-2.5 text-center inline-flex items-center h-full"
              >
                ยกเลิก
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import backend_navbar from "@/components/backend/navbar.vue";
import Modal from "@/components/backend/modal.vue";
import pagination from "@/components/backend/paging.vue";
import FlatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";
import { Thai } from "flatpickr/dist/l10n/th.js";

export default {
  components: { backend_navbar, Modal, pagination, FlatPickr },
  data() {
    return {
      baseUrl: __BASE_URL__,
      apiUrl: __API_URL__,
      imageUrl: __IMAGE_URL__,
      searchText: "",
      searchDataProduct: "",

      products: [],
      productId: "",
      product: {
        id: "",
        code: "",
        name: "",
        cost: "",
        price: "",
        category_id: "",
        status: "",
        detail: "",
        images: [],
      },

      categorys: [],
      categoryStatus: "",
      previewImages: [],

      recommendId: "",
      recommends: [],
      recommendStatus: "",
      recommend: {
        id: "",
        product_id: "",
        start_date: "",
        end_date: "",
        status: "",
      },

      dataPaging: {
        pageNumber: 1,
        rows: 5,
        totalPage: 0,
        status: "",
      },
      totalList: [],

      startDateConfig: {
        locale: Thai,
        dateFormat: "Y-m-d",
        enableTime: false,
        minDate: null, // ไม่จำกัดวันที่เริ่มต้น
        maxDate: null, // ไม่จำกัดวันที่สิ้นสุด
        disableMobile: true, // เปิดใช้งานบนมือถือ
        allowInput: false, // อนุญาตให้พิมพ์วันที่ได้
        monthSelectorType: "dropdown", // แสดงเดือนเป็น dropdown
        yearSelectorType: "dropdown", // แสดงปีเป็น dropdown
        onChange: this.onStartDateChange,
      },
      endDateConfig: {
        locale: Thai,
        dateFormat: "Y-m-d",
        enableTime: false,
        minDate: null,
        maxDate: null,
        disableMobile: true,
        allowInput: false,
        monthSelectorType: "dropdown",
        yearSelectorType: "dropdown",
        onChange: this.onEndDateChange,
      },

      isFocus: false,
      formTable: true,
      formAdd: false,
      formEdit: false,

      DropdownStatusName: "ทั้งหมด",
      DropdownStatusOpen: false,

      pageSizeOpen: false,
    };
  },
  mounted() {
    this.checkAuth();
    document.addEventListener("click", this.closeDropdownStatus);
    document.addEventListener("click", this.closeDropdown);
  },

  methods: {
    checkAuth() {
      const adminRole = localStorage.getItem("admin_role");

      if (adminRole !== "admin") {
        this.$router.push("/backend/login");
      } else {
        this.getListRecommend();
        this.getListCategory();
      }
    },
    showFormTable() {
      this.formTable = true;
      this.formAdd = false;
      this.formEdit = false;
      this.dataPaging.pageNumber = 1;
      this.getListRecommend();
    },

    //เเสดงข้อมูลสินค้าเเนะนำบนตาราง
    async getListRecommend() {
      await axios
        .get(`${this.apiUrl}recommends/`, {
          params: {
            limit: this.dataPaging.rows,
            page: this.dataPaging.pageNumber,
            q: this.searchText,
            status: this.recommendStatus,
          },
        })
        .then((response) => {
          const data = response.data;
          this.recommends = data.rows;
          this.totalList = data.total;

          console.log("recommends", this.recommends);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },
    reloadData(pageNo) {
      this.dataPaging.pageNumber = pageNo;
      this.getListRecommend();

      console.log("pageNo", pageNo);
    },
    pageSize(row) {
      // ตรวจสอบว่าค่า row ใหม่ไม่เท่ากับค่าเดิม
      if (this.dataPaging.rows !== row) {
        this.dataPaging.pageNumber = 1;
        this.dataPaging.rows = row;
        this.getListRecommend();
        this.pageSizeOpen = false;
      }
    },
    searchRecommend() {
      this.dataPaging.pageNumber = 1;
      this.getListRecommend();
      this.$refs.paginationRef.resetPage();
    },
    xmark() {
      this.searchText = "";
      this.dataPaging.pageNumber = 1;
      this.getListRecommend();
      this.$refs.paginationRef.resetPage();
    },

    showFormAdd() {
      this.formTable = false;
      this.formAdd = true;
      this.formEdit = false;
      // this.getListCategory();

      this.searchDataProduct = "";
      this.recommend.start_date = "";
      this.recommend.end_date = "";
      this.recommend.status = "";

      this.product.id = "";
      this.product.code = "";
      this.product.name = "";
      this.product.cost = "";
      this.product.price = "";
      this.product.category_id = "";
      this.product.status = "";
      this.product.detail = "";
      this.product.images = [];
    },

    searchProduct() {
      axios
        .get(`${this.apiUrl}products/search/`, {
          params: {
            q: this.searchDataProduct,
          },
        })
        .then((response) => {
          this.products = response.data.rows;

          console.log(this.products);
        })
        .catch((error) => {
          console.error("There was an error!", error);
        });
    },
    clickProduct(product) {
      this.products = [];
      this.searchDataProduct = "";
      this.product.id = product.id;
      this.product.code = product.code;
      this.product.name = product.name;
      this.product.cost = product.cost;
      this.product.price = product.price;
      this.product.category_id = product.category_id;
      this.product.status = product.status;
      this.product.detail = product.detail;
      this.product.images = product.images;
    },

    async showFormEdit(recommendId) {
      // เปิดฟอร์มแก้ไข
      this.formTable = false;
      this.formAdd = false;
      this.formEdit = true;
      // this.previewImages = [];
      // this.getListCategory();

      try {
        // เรียก API เพื่อดึงข้อมูลสินค้าที่ระบุ
        const response = await axios.get(
          `${this.apiUrl}recommends/${recommendId}`
        );

        // ตรวจสอบว่าข้อมูลของสินค้าได้รับมาอย่างถูกต้อง
        if (response.status === 200) {
          const recommend = response.data.row; // แก้จาก row เป็น data

          if (recommend) {
            this.recommend.id = recommendId;
            this.product.id = recommend.product_id;
            this.product.code = recommend.code;
            this.product.name = recommend.name;
            this.product.cost = recommend.cost;
            this.product.price = recommend.price;
            this.product.category_id = recommend.category_id;
            this.product.status = recommend.product_status;
            this.product.detail = recommend.detail;
            this.product.images = recommend.images;
            this.recommend.start_date = recommend.start_date;
            this.recommend.end_date = recommend.end_date;
            this.recommend.status = recommend.status;

            // ตรวจสอบ category_id
            if (
              !this.categorys.some(
                (category) => category.id === this.product.category_id
              )
            ) {
              this.product.category_id = "";
            }

            // แสดงข้อมูลสินค้าใน console
            console.log("Recommend Data:", recommend);
          } else {
            alert("ไม่พบข้อมูลสินค้าที่ต้องการแก้ไข");
          }
        } else {
          alert(`Failed to fetch recommend details: ${response.statusText}`);
        }
      } catch (error) {
        console.error(
          `Error fetching recommend ${recommendId} from ${this.apiUrl}recommends/${recommendId}:`,
          error.response?.data?.detail || error.message
        );
        this.$refs.modal.showAlertModal({
          swlIcon: "error",
          swlTitle: "ล้มเหลว",
          swlText: "เกิดข้อผิดพลาด",
        });
      } finally {
        // Set loading state to false
        this.loading = false;
      }
    },

    //เเสดงข้อมูลหมวดหมู่สินค้า
    async getListCategory() {
      this.categoryStatus = "active";

      await axios
        .get(`${this.apiUrl}category/`, {
          params: { category_status: this.categoryStatus },
        })
        .then((response) => {
          const data = response.data;
          this.categorys = data.rows;

          console.log("categorys =", this.categorys);
        })
        .catch((error) => {
          console.error("There was an error fetching the data:", error);
        });
    },

    async btnAdd() {
      // ตรวจสอบความครบถ้วนของข้อมูล
      if (!this.product.id) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกสินค้า",
        });
      } else if (!this.recommend.start_date) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกวันที่เริ่มต้นการเเนะนำ",
        });
      } else if (!this.recommend.end_date) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกวันที่สิ้นสุดการเเนะนำ",
        });
      } else if (!this.recommend.status) {
        this.isFocus = true;
        this.$refs.inputStatusRecommend.focus();
      } else {
        try {
          const dataRecommend = {
            product_id: this.product.id,
            start_date: this.recommend.start_date,
            end_date: this.recommend.end_date,
            status: this.recommend.status,
          };

          const response = await axios.post(
            `${this.apiUrl}recommends/`,
            dataRecommend
          );

          if (response.status === 200) {
            this.$refs.modal.showAlertModal({
              swlIcon: "success",
              swlTitle: "สำเร็จ",
              swlText: response.data.message,
            });
          }
        } catch (error) {
          // หากเกิดข้อผิดพลาดในการส่งข้อมูล
          if (error.response && error.response.status === 400) {
            // แสดงข้อความแจ้งเตือนหากมีสินค้านี้อยู่แล้ว
            this.$refs.modal.showModal({
              swlIcon: "info",
              swlTitle: "เเจ้งเตือน",
              swlText: error.response.data.detail,
            });
          } else {
            this.$refs.modal.showAlertModal({
              swlIcon: "error",
              swlTitle: "เกิดข้อผิดพลาด",
              swlText: error.message,
            });
          }
        }
      }
    },

    async btnEdit() {
      if (!this.product.id) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกสินค้า",
        });
      } else if (!this.recommend.start_date) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกวันที่เริ่มต้นการเเนะนำ",
        });
      } else if (!this.recommend.end_date) {
        this.$refs.modal.showModal({
          swlIcon: "info",
          swlTitle: "กรุณาเลือกวันที่สิ้นสุดการเเนะนำ",
        });
      } else if (!this.recommend.status) {
        this.isFocus = true;
        this.$refs.inputStatusRecommend.focus();
      } else {
        try {
          const dataRecommend = {
            product_id: this.product.id,
            start_date: this.recommend.start_date,
            end_date: this.recommend.end_date,
            status: this.recommend.status,
          };

          const response = await axios.put(
            `${this.apiUrl}recommends/${this.recommend.id}`,
            dataRecommend
          );
          if (response.status === 200) {
            this.$refs.modal.showAlertModal({
              swlIcon: "success",
              swlTitle: "สำเร็จ",
              swlText: response.data.message,
            });
          }
        } catch (error) {
          this.$refs.modal.showAlertModal({
            swlIcon: "error",
            swlTitle: "เกิดข้อผิดพลาด",
            swlText: error,
          });
        }
      }
    },

    btnDelete(recommendId) {
      // เรียกใช้งาน modal เพื่อแสดงคำเตือน
      this.$refs.modal.showDeleteModal({
        swlIcon: "warning",
        swlTitle: "แจ้งเตือน",
        swlText: "คุณต้องการลบสินค้านี้หรือไม่!",
        onConfirm: () => {
          // เมื่อผู้ใช้กด "ยืนยัน" ใน modal
          axios
            .delete(`${this.apiUrl}recommends/${recommendId}`)
            .then((response) => {
              // แสดงข้อความว่า "ลบสำเร็จ"
              this.$swal
                .fire({
                  title: "ลบสำเร็จ",
                  icon: "success",
                  confirmButtonText: "ยืนยัน",
                  customClass: {
                    confirmButton:
                      "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
                  },
                })
                .then(() => {
                  // เมื่อกดปุ่ม "ยืนยัน" ใน swal ที่สอง
                  this.showFormTable();
                });
            })
            .catch((error) => {
              console.error("Error updating product status:", error);
              this.$swal.fire({
                title: "เกิดข้อผิดพลาด",
                text: "ไม่สามารถอัปเดตสถานะสินค้าได้",
                icon: "error",
                confirmButtonText: "ยืนยัน",
                customClass: {
                  confirmButton:
                    "bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400",
                },
              });
            });
        },
      });
    },

    onStartDateChange(selectedDates) {
      if (selectedDates[0]) {
        this.endDateConfig.minDate = selectedDates[0];
      }
    },
    onEndDateChange(selectedDates) {
      if (selectedDates[0]) {
        this.startDateConfig.maxDate = selectedDates[0];
      }
    },

    inputImage(event) {
      const files = event.target.files;
      this.previewImages = [];

      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        if (file && file.type.startsWith("image")) {
          const reader = new FileReader();
          reader.onload = (e) => {
            const imageURL = e.target.result;
            this.previewImages.push(imageURL);
            console.log("Image URL:", imageURL);
          };
          reader.readAsDataURL(file);
        }
      }
      console.log(this.previewImages);
    },

    validateNumberInput(event) {
      // กรองค่าให้เป็นตัวเลขและทศนิยม
      let value = event.target.value;
      value = value.replace(/[^0-9.]/g, ""); // เอาตัวอักษรที่ไม่ใช่ตัวเลขและจุดทศนิยมออก
      const decimalCount = (value.match(/\./g) || []).length;
      if (decimalCount > 1) {
        value = value.slice(0, value.lastIndexOf("."));
      }
      event.target.value = value; // อัพเดตค่าใน input element
      this.product[event.target.name] = value; // อัพเดตข้อมูลใน model (product.cost หรือ product.price)
    },

    ///// {{ DropdownStatus }} /////
    DropdownStatus(status, name) {
      this.recommendStatus = status;
      this.dataPaging.pageNumber = 1;
      this.getListRecommend();
      this.DropdownStatusName = name;
      if (status === "" || name === "") {
        this.DropdownStatusName = "ทั้งหมด";
      }
      this.DropdownStatusOpen = false;
      this.$refs.paginationRef.resetPage();
      console.log("DropdownStatus", status, name);
    },
    clickDropdownStatus(event) {
      // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
      event.stopPropagation();
      this.DropdownStatusOpen = !this.DropdownStatusOpen;
    },
    closeDropdownStatus(event) {
      // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
      const dropdown = this.$refs.statusMenu;
      if (dropdown && !dropdown.contains(event.target)) {
        this.DropdownStatusOpen = false;
      }
    },

    togglePageSize(event) {
      // ป้องกันการคลิกบนปุ่มที่ทำให้ event ไปถึง listener ของ document
      event.stopPropagation();
      this.pageSizeOpen = !this.pageSizeOpen;
    },
    closeDropdown(event) {
      // ตรวจสอบว่าคลิกภายนอกปุ่มและ dropdown หรือไม่
      const dropdown = this.$refs.pageSizeMenu;
      if (dropdown && !dropdown.contains(event.target)) {
        this.pageSizeOpen = false;
      }
    },
  },
};
</script>
