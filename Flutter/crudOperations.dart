import 'package:notes/notes_model.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

final String tableName = 'Notes';

class NotesDatabase {
  Future<Database> initializeDB() async {
    String path = await getDatabasesPath();

    return openDatabase(
        join(path, 'NotesDB.db'),
        version: 1,
        onCreate: (Database db, int version) async {
          await db.execute('''create table $tableName (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)''');
        });
  }

  Future<int> insert(List<Notes> notes) async {
    int result = 0;
    final Database db = await initializeDB();
    for(var note in notes) {
      result = await db.insert(tableName, note.toMap());
    }
    return result;
  }

  Future<List<Notes>> getNotes() async {
    final Database db = await initializeDB();
    final List<Map<String, Object?>> queryResult = await db.query(tableName);
    return queryResult.map((e) => Notes.fromMap(e)).toList();
  }

  Future<void> delete(int id) async {
    final db = await initializeDB();
    await db.delete(tableName, where: 'id = ?', whereArgs: [id]);
  }
}
