import mongoose from 'mongoose'

const Site = mongoose.createschema({
    siteName: {
        type: String,
        required: true
    },
    products: [
        {
            storage: {
                type: String,
                enum: ['IBM', 'Dell'],
                required: true
            },
            storageType: {
                type: String,
                enum: ['RAM', 'Hard Disk'],
                required: true
            },
            capacityGB: {
                type: String,
                required: true,
            },
            speed: {
                type: String,
                required:true
        }

        }
    ]
})