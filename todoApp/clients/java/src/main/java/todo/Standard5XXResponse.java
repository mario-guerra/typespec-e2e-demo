package todo;

import io.clientcore.core.annotations.Metadata;
import io.clientcore.core.annotations.TypeConditions;
import io.clientcore.core.serialization.json.JsonReader;
import io.clientcore.core.serialization.json.JsonToken;
import io.clientcore.core.serialization.json.JsonWriter;
import java.io.IOException;

/**
 * Something is wrong with me.
 */
@Metadata(conditions = { TypeConditions.IMMUTABLE })
public final class Standard5XXResponse extends ApiError {
    /**
     * Creates an instance of Standard5XXResponse class.
     * 
     * @param code the code value to set.
     * @param message the message value to set.
     */
    @Metadata(generated = true)
    private Standard5XXResponse(String code, String message) {
        super(code, message);
    }

    /**
     * {@inheritDoc}
     */
    @Metadata(generated = true)
    @Override
    public JsonWriter toJson(JsonWriter jsonWriter) throws IOException {
        jsonWriter.writeStartObject();
        jsonWriter.writeStringField("code", getCode());
        jsonWriter.writeStringField("message", getMessage());
        return jsonWriter.writeEndObject();
    }

    /**
     * Reads an instance of Standard5XXResponse from the JsonReader.
     * 
     * @param jsonReader The JsonReader being read.
     * @return An instance of Standard5XXResponse if the JsonReader was pointing to an instance of it, or null if it was
     * pointing to JSON null.
     * @throws IllegalStateException If the deserialized JSON object was missing any required properties.
     * @throws IOException If an error occurs while reading the Standard5XXResponse.
     */
    @Metadata(generated = true)
    public static Standard5XXResponse fromJson(JsonReader jsonReader) throws IOException {
        return jsonReader.readObject(reader -> {
            String code = null;
            String message = null;
            while (reader.nextToken() != JsonToken.END_OBJECT) {
                String fieldName = reader.getFieldName();
                reader.nextToken();

                if ("code".equals(fieldName)) {
                    code = reader.getString();
                } else if ("message".equals(fieldName)) {
                    message = reader.getString();
                } else {
                    reader.skipChildren();
                }
            }
            return new Standard5XXResponse(code, message);
        });
    }
}
